import requests
from requests.auth import HTTPBasicAuth
import json

# Jira Configuration
JIRA_URL = "https://spubmath.atlassian.net"
API_TOKEN = {secrets.API_TOKEN}
EMAIL = {secrets.EMAIL}
auth = HTTPBasicAuth(EMAIL, API_TOKEN)
PROJECT_KEY = "SCRUM"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def update_issue_status(issue_key, transition_id):
    """
    Transition an issue to a new status.
    """
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}/transitions"
    payload = {
        "transition": {
            "id": transition_id
        }
    }

    response = requests.post(url, headers=headers, auth=auth, json=payload)

    if response.status_code == 204:
        print(f"Issue {issue_key} status updated successfully!")
    else:
        print(f"Failed to update issue {issue_key} status: {response.status_code} {response.text}")

