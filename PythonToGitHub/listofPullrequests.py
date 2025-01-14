import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_data = response.json()


for i in range(len(complete_data)):
    print("User Login : ", complete_data[i]["user"]["login"])
    print("User Created at: ",complete_data[i]["created_at"])


