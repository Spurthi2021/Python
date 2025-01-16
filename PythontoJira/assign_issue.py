import requests
from requests.auth import HTTPBasicAuth
import json
from get_user_account_id import get_user_account_id
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Jira Configuration
JIRA_URL = "https://spubmath.atlassian.net"
API_TOKEN = os.getenv("API_KEY")
EMAIL = os.getenv("EMAIL"}
auth = HTTPBasicAuth(EMAIL, API_TOKEN)
PROJECT_KEY = "SCRUM"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def assign_issue(issue_key, assignee_email):
    """
    Assign an issue to a user.
    """
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/assignee"
    payload = {
        "accountId": get_user_account_id(assignee_email)
    }

    response = requests.put(url, headers=headers, auth=auth, json=payload)

    if response.status_code == 204:
        print(f"Issue {issue_key} assigned to {assignee_email} successfully!")
    else:
        print(f"Failed to assign issue {issue_key}: {response.status_code} {response.text}")

