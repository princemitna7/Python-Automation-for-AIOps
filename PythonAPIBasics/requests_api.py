import requests

url = "https://api.github.com/repos/kodekloudhub/git-for-beginners-course"
response = requests.get(url)
repo = response.json()

print(f"{repo["name"]} - Created at: {repo["created_at"]}")  # prints all fields; you need to modify this