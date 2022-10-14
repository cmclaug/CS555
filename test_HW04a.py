import unittest
#from unittest import mock
import requests
import json

class FakeResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

switcher = {
    'https://api.github.com/users/richkempinski/repos':'mockRepoInfo.json',cd
    'https://api.github.com/repos/richkempinski/csp/commits':'mockRepoCommits.json'
}

def mocked_requests_get(*args):
    if args[0] in switcher:
        with open(switcher[args[0]]) as f:
            return FakeResponse(json.load(f))
    return FakeResponce(None)

def gitHubResults(userID):
    x = requests.get("https://api.github.com/users/" + userID + "/repos")
    x = x.json()
    result = ""
    for i in x:
        result = result + "Repo: " + i["name"]
        y = requests.get("https://api.github.com/repos/" + userID + "/" + i["name"] + "/commits")
        y = y.json()
        result = result + " Number of commits: " + str(len(y)) + "\n"
    return result[:-1]

class Test(unittest.TestCase):
    def test_gitHubResults(self):
        self.assertEqual(gitHubResults("richkempinski"), "\nRepo: csp Number of commits: 2")