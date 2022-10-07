"""
Author Name: Saurabh Agrawal
HW 04a: Develop with the Perspective of the Tester in mind
"""

import requests
import json
from constants import GITHUB_URL, USERS, REPOS, SLASH, COMMITS

def githubapi(usernm):
    response = requests.get(GITHUB_URL + USERS + SLASH + usernm + REPOS)

    if response.status_code != 200:
        print("No Account with this name")
        return False

    response = response.json()

    if len(response) == 0:
        print("There is no repository with this name")
        return False
    
    for repo in response:
        repoResponse = requests.get(repo['commits_url'].split("{")[0])
        repoResponse = repoResponse.json()
        print("Repository Name: "+ repo['name'] + " \t\t\t\tNumber Of Commits: " + str(len(repoResponse)))

    return True

if __name__ == '__main__':
    userInput = input("Enter Github username: ")
    githubapi(userInput)
