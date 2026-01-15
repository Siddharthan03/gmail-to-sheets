📧 Gmail to Google Sheets Automation
👤 Author

Name: Siddharthan

Language: Python 3

APIs Used: Gmail API, Google Sheets API

Authentication: OAuth 2.0 (Installed App Flow)

📖 Project Overview

1. Python automation to read real unread Gmail emails

2. Logs email data into Google Sheets

3. Each email is stored as a new row

4. System is idempotent (no duplicate rows on re-run)

      Data logged per email:

5. Sender email address

6. Subject

7. Date & time received

8. Email body (plain text)

🎯 Project Objectives

1. Authenticate Gmail using OAuth 2.0

2. Fetch unread emails from Inbox

3. Parse email metadata and content

4. Append email data to Google Sheets

5. Mark processed emails as read

6. Prevent duplicate processing on subsequent runs

🏗️ High-Level Architecture

1. Gmail Inbox → Gmail API (OAuth)

2. Python automation script

3. Google Sheets API → Google Sheet storage

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

1. Create a Google Cloud project

2. Enable:

      . Gmail API

      . Google Sheets API

3. Configure OAuth Consent Screen:

4. User type: External

5. Add your Gmail ID as a Test User

6. Create OAuth Client ID:

7. Application type: Desktop

8. Download credentials.json

9. Place it in:
    
      credentials/credentials.json
⚠️ This file is intentionally excluded from GitHub.

5️⃣ Run the Script:

      python3 -m src.main


First run behavior:

1. Browser opens for OAuth consent

2. User grants permissions

3. Access token generated

4. Emails processed and logged

🔐 OAuth Flow Explanation

1. Uses OAuth 2.0 Installed App flow

2. User explicitly authorizes Gmail and Sheets access

3. Token stored locally as token.json

4. No API keys or service accounts used

5. Required due to Gmail’s sensitive data access rules

🔁 Duplicate Prevention Logic

1. Each Gmail email has a unique message ID

2. Processed message IDs stored in state.json

3. On each run:

      . Script checks if message ID already exists

      . If yes → email is skipped

4. Result:

   No duplicate rows

Safe re-execution of script

🗂️ State Persistence Method

1. State stored in state.json

2. Contains list of processed Gmail message IDs

3. Chosen because:

      . Simple and lightweight

      . No database required

      . Gmail message IDs are immutable

📸 Proof of Execution

1. The /proof folder contains:

      . Gmail Inbox screenshot (unread emails)

      . Google Sheet screenshot (minimum 5 rows)

      . OAuth consent screen screenshot

2. 2–3 minute demo video explaining:

      . Project flow

      . Gmail → Sheets integration

      . Duplicate prevention

      . Script re-run behavior

⚠️ Challenges Faced & Solutions
1. Challenge

      . OAuth access blocked due to testing mode

      . Gmail and Sheets APIs initially disabled

2. Solution

      . Added Gmail account as Test User

      . Enabled required APIs explicitly

      . Allowed propagation time for API activation

3. 📉 Limitations

      . Google Sheets has a 50,000 character cell limit

      . Long email bodies are truncated with [TRUNCATED]

      . Email content stored as plain text

      . HTML emails cleaned but not visually formatted

      . Attachments are not processed


🔄 Post-Submission Modification Readiness

1. Project structure supports easy changes such as:

2. Filtering emails from last 24 hours

3. Adding new columns (labels, thread ID)

4. Excluding automated emails (no-reply)

✅ Conclusion

This project demonstrates:

      . Real-world API integration
      
      . Secure OAuth 2.0 handling
      
      . Idempotent automation design
      
      . Clean and maintainable Python code
