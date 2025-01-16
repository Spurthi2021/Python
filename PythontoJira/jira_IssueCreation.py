# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

from create_Issue import create_Issue 

project_Key = input("Enter the Project Key : ")
print( "These are list of Issue Types you can create, Please select the required one : \n 1. Task \n 2. Story \n 3. Bug \n 4. Epic ")
issue_type = input("Enter the Issue Type you want create : ")

if issue_type.lower() == "task":
    issue_type_id = 10005      
elif issue_type.lower() == "story":
    issue_type_id = 10007       
elif issue_type.lower() == "epic":
    issue_type_id = 10008      
elif issue_type.lower() == "bug":
    issue_type_id = 10006        
else:
    print("There is no such Issue type")
    issue_type_id = 0   

if issue_type_id == 0:
    print("There is no Such Issue Type. Hence cant create Issue.")
else:
    no_of_issues = int(input("Enter the number of Issues to be created of this Issue Type : "))
    create_Issue(project_Key, issue_type_id, no_of_issues)
