import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

def get_user_account_id(email):
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


    """
    Get a user's account ID from their email.
    """
    url = f"{JIRA_URL}/rest/api/3/user/search"
    params = {
        "query": email
    }

    response = requests.get(url, headers=headers, auth=auth, params=params)

    if response.status_code == 200:
        users = response.json()
        if users:
            return users[0]["accountId"]
        else:
            print(f"No user found for email: {email}")
            return None
    else:
        print(f"Failed to fetch user account ID: {response.status_code} {response.text}")
        return None
