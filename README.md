📧 Gmail to Google Sheets Automation

Author: Siddharthan
Language: Python 3
APIs Used: Gmail API, Google Sheets API
Authentication: OAuth 2.0 (Installed App Flow)

📖 Project Overview

This project is a Python automation system that reads real unread emails from a Gmail inbox and logs them into a Google Sheet in a structured format.

Each qualifying email is added as a new row containing:

Sender email address

Subject

Date & time received

Email body (plain text)

The system is designed to be idempotent, meaning re-running the script does not duplicate data.

🎯 Objective

Connect to Gmail using OAuth 2.0

Fetch unread emails from the Inbox

Parse email metadata and content

Append data into Google Sheets

Mark processed emails as read

Prevent duplicate processing on re-runs

🏗️ High-Level Architecture

┌──────────┐
│  Gmail   │
│  Inbox   │
└────┬─────┘
     │  Gmail API (OAuth)
     ▼
┌───────────────┐
│ Python Script │
│ (Parsing +    │
│ State Logic)  │
└────┬──────────┘
     │  Google Sheets API
     ▼
┌────────────────────┐
│ Google Sheets      │
│ Gmail Inbox Logs   │
└────────────────────┘


📂 Project Structure

gmail-to-sheets/
│
├── src/
│   ├── __init__.py
│   ├── gmail_service.py
│   ├── sheets_service.py
│   ├── email_parser.py
│   └── main.py
│
├── credentials/
│   └── credentials.json   (NOT committed)
│
├── proof/
│   ├── gmail_unread.png
│   ├── google_sheet.png
│   ├── oauth_consent.png
│   └── demo_video.mp4
│
├── config.py
├── requirements.txt
├── .gitignore
└── README.md


⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd gmail-to-sheets

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Google Cloud Setup

Create a Google Cloud project

Enable:

Gmail API

Google Sheets API

Configure OAuth Consent Screen

Type: External

Add your Gmail ID as a Test User

Create OAuth Client ID

Application type: Desktop

Download credentials.json

Place it in:

credentials/credentials.json


⚠️ This file is intentionally excluded from GitHub.

5️⃣ Run the Script
python3 -m src.main


On first run:

Browser opens for OAuth consent

Access token is generated

Emails are processed

🔐 OAuth Flow Explanation

Uses OAuth 2.0 Installed App flow

User explicitly grants Gmail & Sheets access

Access token is stored locally in token.json

No API keys or service accounts are used

This is required because Gmail data is sensitive and cannot be accessed via service accounts.

🔁 Duplicate Prevention Logic

Every processed email has a unique Gmail message ID

Processed IDs are stored in state.json

On each run:

Script checks if an email ID already exists

If yes → it is skipped

This ensures:

No duplicate rows

Safe re-execution of the script

🗂️ State Persistence Method

State is stored in a local file: state.json

Contains a list of processed Gmail message IDs

Chosen because:

Simple

Lightweight

No database required

Gmail message IDs are immutable

📸 Proof of Execution

The /proof folder contains:

Gmail Inbox Screenshot

Showing unread emails

Google Sheet Screenshot

At least 5 rows populated by the script

OAuth Consent Screen Screenshot

2–3 Minute Demo Video

Explains project flow

Shows duplicate prevention

Explains re-run behavior

⚠️ Challenges Faced & Solutions
Challenge:

Google OAuth initially blocked access due to testing mode and disabled APIs.

Solution:

Added Gmail account as a Test User

Enabled Gmail API and Google Sheets API explicitly

Allowed propagation time for API activation

📉 Limitations

Google Sheets has a 50,000 character limit per cell

Long email bodies are truncated safely with a [TRUNCATED] marker

Email formatting is plain text

HTML emails are converted to text and lightly cleaned

Attachments are not processed

⭐ Bonus Enhancements Implemented

HTML → plain text conversion

Email body cleaning

Safe truncation for large emails

Robust error handling

Clean project structure

🔄 Post-Submission Modification Readiness

The project is structured to easily support changes such as:

Filtering emails from last 24 hours

Adding new columns (labels, thread ID)

Excluding automated emails (no-reply)

✅ Conclusion

This project demonstrates:

Real-world API integration

Secure OAuth handling

Idempotent automation design

Clean and maintainable Python code