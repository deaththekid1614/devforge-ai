import requests

def fetch_github_repos(query):

    url = f"https://api.github.com/search/repositories?q={query}+language:python&sort=stars&order=desc&per_page=12"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    repos = []

    for repo in data.get("items", []):

        description = repo["description"]

        # skip repos with bad descriptions
        if not description:
            continue

        # ignore non-english spam
        if any(ord(char) > 128 for char in description):
            continue

        repos.append({
            "name": repo["name"],
            "description": description[:120],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "language": repo["language"]
        })

    return repos[:6]
