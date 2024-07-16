"""Tiny script to clean Github labels for a repository matching a pattern.

Doesn't support pagination, but could easily be added.
Github API documentation: https://docs.github.com/en/rest/issues/labels?apiVersion=2022-11-28#list-labels-for-a-repository
"""
import re

from httpx import Client

pat = ""
org = ""
repo = ""
delete_label_pattern = ""

client = Client(
    headers={
        "Authorization": f"Bearer {pat}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
)
response = client.get(
    f"https://api.github.com/repos/{org}/{repo}/labels", params={"per_page": 100}
)
labels = response.json()
for i, label in enumerate(labels):
    if (name := label["name"]) and re.match(delete_label_pattern, name):
        r = client.delete(f"https://api.github.com/repos/{org}/{repo}/labels/{name}")
        r.raise_for_status()
        print(f"Deleted label {i}: {name}")
