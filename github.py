import requests

# This is a FAKE token for demonstration purposes only
token = "ghp_MOCKTOKEN1234567890abcdef1234567890abcdef"
headers = {
    "Authorization": f"token {token}",
    "User-Agent": "ExampleApp"
}

response = requests.get("https://api.github.com/user/repos", headers=headers)
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(repo['name'])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}. Message: {response.text}")
