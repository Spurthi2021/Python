import requests
from requests.auth import HTTPBasicAuth
import json
from assign_issue import assign_issue
from search_issues import search_issues
from update_issue_status import update_issue_status



def main():
    # Define a JQL query to fetch issues (customize this query)
    jql_query = f"project = {PROJECT_KEY} AND status = 'To Do'"

    # Search for issues
    issues = search_issues(jql_query)

    # Process each issue
    for issue in issues:
        issue_key = issue["key"]
        issue_status = issue["fields"]["status"]["name"]
        assignee = issue["fields"]["assignee"]

        print(f"Processing issue: {issue_key}, Status: {issue_status}, Assignee: {assignee}")

        #  Update status if it's in "To Do", 11 is for TO-D0
        if issue_status == "To Do":
            transition_id = "11"  
            update_issue_status(issue_key, transition_id)

        # Assign issue if unassigned
        if assignee is None:
            assign_issue(issue_key, "spu.b.math@gmail.com")  


if __name__ == "__main__":
    main()
