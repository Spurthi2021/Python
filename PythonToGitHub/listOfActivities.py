import requests

#List of Activities on a Repo

activities = requests.get("https://api.github.com/repos/Spurthi2021/Python/activity")

list_of_activities = activities.json()

for aa in range(len(list_of_activities)):
    print("List of Activities Timestamp :", list_of_activities[i]["timestamp"])
    print("List of Activities Type:", list_of_activities[i]["activity_type"])
    print("List of Activities Actor ID:", list_of_activities[i]["actor"]["id"])
