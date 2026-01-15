import json
import os
from .gmail_service import get_gmail_service, fetch_unread_emails, mark_as_read
from .email_parser import parse_email
from .sheets_service import get_sheets_service, create_spreadsheet, append_row
from config import STATE_FILE


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"processed_ids": []}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def main():
    gmail = get_gmail_service()
    sheets = get_sheets_service()

    state = load_state()
    processed = set(state["processed_ids"])

    spreadsheet_id = create_spreadsheet(sheets)

    messages = fetch_unread_emails(gmail)

    for msg in messages:
        if msg["id"] in processed:
            continue

        email = parse_email(gmail, msg["id"])

        append_row(
            sheets,
            spreadsheet_id,
            [
                email["from"],
                email["subject"],
                email["date"],
                email["content"]
            ]
        )

        mark_as_read(gmail, msg["id"])
        processed.add(msg["id"])

    state["processed_ids"] = list(processed)
    save_state(state)

    print("✅ All unread emails processed successfully")


if __name__ == "__main__":
    main()
