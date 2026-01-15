import base64
import re
from bs4 import BeautifulSoup


def _decode(data):
    return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")


def extract_body(payload):
    """
    Recursively extract email body.
    Prefer text/plain, fallback to cleaned text/html.
    """

    texts = []

    # If this part has body data
    if payload.get("body", {}).get("data"):
        texts.append(_decode(payload["body"]["data"]))

    # If this part has sub-parts, recurse
    for part in payload.get("parts", []):
        mime = part.get("mimeType", "")

        if mime == "text/plain" and part.get("body", {}).get("data"):
            return _decode(part["body"]["data"])

        if mime == "text/html" and part.get("body", {}).get("data"):
            html = _decode(part["body"]["data"])
            soup = BeautifulSoup(html, "html.parser")

            for tag in soup(["script", "style"]):
                tag.decompose()

            texts.append(soup.get_text(separator="\n"))

        # Recurse into nested multiparts
        texts.append(extract_body(part))

    return "\n".join(t for t in texts if t)


def clean_text(text):
    if not text:
        return ""

    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        lower = line.lower()

        # Soft filtering (do NOT over-delete)
        if lower.startswith("unsubscribe"):
            continue
        if "view in browser" in lower:
            continue

        cleaned_lines.append(line)

    # 🔐 SAFETY: if cleaning removes everything, return original text
    if not cleaned_lines:
        return text.strip()

    cleaned_text = "\n".join(cleaned_lines)

    # Normalize spacing
    cleaned_text = re.sub(r"\n{3,}", "\n\n", cleaned_text)

    return cleaned_text.strip()


def parse_email(service, msg_id):
    message = service.users().messages().get(
        userId="me",
        id=msg_id,
        format="full"
    ).execute()

    headers = {
        h["name"]: h["value"]
        for h in message["payload"]["headers"]
    }

    raw_body = extract_body(message["payload"])
    clean_body = clean_text(raw_body)

    # 🔐 Google Sheets cell limit protection
    MAX_CELL_LENGTH = 45000
    if len(clean_body) > MAX_CELL_LENGTH:
        clean_body = clean_body[:MAX_CELL_LENGTH] + "... [TRUNCATED]"

    return {
        "id": msg_id,
        "from": headers.get("From", ""),
        "subject": headers.get("Subject", ""),
        "date": headers.get("Date", ""),
        "content": clean_body
    }
