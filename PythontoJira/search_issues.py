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

def search_issues(jql_query):
    url = f"{JIRA_URL}/rest/api/3/search"
    params = {
        "jql": jql_query,
        "fields": "id,key,status,assignee"
    }

    response = requests.get(url, headers=headers, auth=auth, params=params)

    if response.status_code == 200:
        issues = response.json().get("issues", [])
        return issues
    else:
        print(f"Failed to search issues: {response.status_code} {response.text}")
        return []

