import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return 0
        else:
            print(f"Error: Unable to fetch data for subreddit '{subreddit}'. Status code: {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
