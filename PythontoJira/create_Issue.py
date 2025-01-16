import requests
from requests.auth import HTTPBasicAuth
import json

def create_Issue(projectKey, issueType, noofIssues) :

    API_TOKEN = {secrets.API_TOKEN}
    EMAIL = {secrets.EMAIL}
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    url = "https://spubmath.atlassian.net/rest/api/3/issue"
    
    issues = noofIssues

    for i in range(noofIssues):

        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        payload = json.dumps( {
            "fields": {
                
                "description": {
                "content": [
                    {
                    "content": [
                        {
                        "text": "This is the issue created via Python code.",
                        "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
                },
                
                "issuetype": {
                "id": issueType
                },
                "project": {
                "key": projectKey
                },
                "summary": "Ticket Created via Python Script",
                
            },
            
            } )

        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
    
        listofissues = json.loads(response.text)
        if "id" in listofissues:
            issue_id = listofissues["id"]
            issue_key = listofissues["key"]
            print(f"Issue created successfully! Issue ID: {issue_id}, Issue Key: {issue_key}")
        else:
            print("Failed to create issue. Response:", listofissues)
