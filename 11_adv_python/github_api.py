# github_api.py
# A program that uses the requests package to fetch data from GitHub's API

import requests

# Define the API endpoint
url = "https://api.github.com/users/octocat"

# Make a GET request
response = requests.get(url)

if response.status_code == 200:
    # Convert the response to a Python dictionary
    data = response.json()
    
    # Print some information from the response
    print(f"Username: {data['login']}")
    print(f"Name: {data['name']}")
    print(f"Public repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print(f"Request failed with status code: {response.status_code}")