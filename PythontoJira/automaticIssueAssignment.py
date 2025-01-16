#Python script to automate the assignment of Jira issues to the appropriate developers or teams.

import requests
from requests.auth import HTTPBasicAuth
import json

# Jira API Credentials
JIRA_URL = https://spubmath.atlassian.net/rest/api/3/issue
API_TOKEN = {secrets.API_TOKEN}
EMAIL = {secrets.EMAIL}
auth = HTTPBasicAuth(EMAIL, API_TOKEN)

assignment_rules = {
    "frontend": "345tfgn6tkujhbjjjk",
    "backend": "876trtyfgfhj98oolikhjh5",
    "database": "4567vghjfi6rfy"
}

def assign_issue(issue_key, component):
    
    if component not in assignment_rules:
        print(f"No rule defined for component: {component}")
        return
    
    assignee = assignment_rules[component]
    url = f"{JIRA_URL}{issue_key}/assignee"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps({"accountId": assignee})

    response = requests.put(url, headers=headers, data=payload, auth=auth)

    if response.status_code == 204:
        print(f"Issue {issue_key} successfully assigned to {assignee}.")
    else:
        print(f"Failed to assign issue {issue_key}. Response: {response.text}")

issue_key = "SCRUM-23"
component = "backend"
assign_issue(issue_key, component)
