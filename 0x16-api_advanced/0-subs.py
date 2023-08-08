import requests

def number_of_subscribers(subreddit):
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data["data"]["subscribers"]
        except KeyError:
            print("Invalid subreddit data format")
            return 0
    elif response.status_code == 404:
        print("Subreddit not found")
        return 0
    else:
        print("Error occurred while fetching subreddit data")
        return 0
