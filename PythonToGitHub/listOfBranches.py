import requests



# List of Branches

branches = requests.get("https://api.github.com/repos/Spurthi2021/MultiBranch1/branches")

list_of_branches = branches.json()

for b in range(len(list_of_branches)):
    print("List of Branches :", list_of_branches[b]["name"])
    print("URL of Branches :", list_of_branches[b]["commit"]["url"])

