📧 Gmail to Google Sheets Automation
👤 Author

Name: Siddharthan

Language: Python 3

APIs Used: Gmail API, Google Sheets API

Authentication: OAuth 2.0 (Installed App Flow)

📖 Project Overview

Python automation to read real unread Gmail emails

Logs email data into Google Sheets

Each email is stored as a new row

System is idempotent (no duplicate rows on re-run)

Data logged per email:

Sender email address

Subject

Date & time received

Email body (plain text)

🎯 Project Objectives

Authenticate Gmail using OAuth 2.0

Fetch unread emails from Inbox

Parse email metadata and content

Append email data to Google Sheets

Mark processed emails as read

Prevent duplicate processing on subsequent runs

🏗️ High-Level Architecture

Gmail Inbox → Gmail API (OAuth)

Python automation script

Google Sheets API → Google Sheet storage

Gmail Inbox
   ↓
Gmail API (OAuth)
   ↓
Python Script (Parsing + State Management)
   ↓
Google Sheets API
   ↓
Google Sheet (Gmail Inbox Logs)

📂 Project Structure
gmail-to-sheets/
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
1️⃣ Clone Repository
git clone <your-repo-url>
cd gmail-to-sheets

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Google Cloud Configuration

Create a Google Cloud project

Enable:

Gmail API

Google Sheets API

Configure OAuth Consent Screen:

User type: External

Add your Gmail ID as a Test User

Create OAuth Client ID:

Application type: Desktop

Download credentials.json

Place it in:

credentials/credentials.json


⚠️ This file is intentionally excluded from GitHub.

5️⃣ Run the Script
python3 -m src.main


First run behavior:

Browser opens for OAuth consent

User grants permissions

Access token generated

Emails processed and logged

🔐 OAuth Flow Explanation

Uses OAuth 2.0 Installed App flow

User explicitly authorizes Gmail and Sheets access

Token stored locally as token.json

No API keys or service accounts used

Required due to Gmail’s sensitive data access rules

🔁 Duplicate Prevention Logic

Each Gmail email has a unique message ID

Processed message IDs stored in state.json

On each run:

Script checks if message ID already exists

If yes → email is skipped

Result:

No duplicate rows

Safe re-execution of script

🗂️ State Persistence Method

State stored in state.json

Contains list of processed Gmail message IDs

Chosen because:

Simple and lightweight

No database required

Gmail message IDs are immutable

📸 Proof of Execution

The /proof folder contains:

Gmail Inbox screenshot (unread emails)

Google Sheet screenshot (minimum 5 rows)

OAuth consent screen screenshot

2–3 minute demo video explaining:

Project flow

Gmail → Sheets integration

Duplicate prevention

Script re-run behavior

⚠️ Challenges Faced & Solutions
Challenge

OAuth access blocked due to testing mode

Gmail and Sheets APIs initially disabled

Solution

Added Gmail account as Test User

Enabled required APIs explicitly

Allowed propagation time for API activation

📉 Limitations

Google Sheets has a 50,000 character cell limit

Long email bodies are truncated with [TRUNCATED]

Email content stored as plain text

HTML emails cleaned but not visually formatted

Attachments are not processed

⭐ Bonus Enhancements Implemented

HTML → plain text conversion

Email body cleaning

Safe truncation for large emails

Robust error handling

Clean, modular project structure

🔄 Post-Submission Modification Readiness

Project structure supports easy changes such as:

Filtering emails from last 24 hours

Adding new columns (labels, thread ID)

Excluding automated emails (no-reply)

✅ Conclusion

This project demonstrates:

Real-world API integration

Secure OAuth 2.0 handling

Idempotent automation design

Clean and maintainable Python code
