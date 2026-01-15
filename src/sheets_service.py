import os
import pickle
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from config import SPREADSHEET_NAME

TOKEN_FILE = "token.json"


def get_sheets_service():
    if not os.path.exists(TOKEN_FILE):
        raise Exception("OAuth token not found. Run Gmail auth first.")

    with open(TOKEN_FILE, "rb") as token:
        creds = pickle.load(token)

    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    return build("sheets", "v4", credentials=creds)


def create_spreadsheet(service):
    spreadsheet = service.spreadsheets().create(
        body={"properties": {"title": SPREADSHEET_NAME}}
    ).execute()

    return spreadsheet["spreadsheetId"]


def append_row(service, spreadsheet_id, row):
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="Sheet1!A:D",
        valueInputOption="RAW",
        body={"values": [row]}
    ).execute()
