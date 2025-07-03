import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:RedditTopTen:1.0 (by u/your_reddit_username)"} # Replace with your Reddit username

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.json()
        posts = data['data']['children']

        if not posts:
            print("No posts found for this subreddit.")
            return

        print(f"Top 10 hot posts for r/{subreddit}:")
        for i, post in enumerate(posts[:10]):
            title = post['data']['title']
            print(f"{i + 1}. {title}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(None)
        else:
            print(f"An HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except KeyError:
        print(None) # Handle cases where the JSON structure might be unexpected (e.g., invalid subreddit returning different data)

if __name__ == '__main__':
    # Example usage:
    top_ten("python")
    print("-" * 20)
    top_ten("learnpython")
    print("-" * 20)
    top_ten("nonexistent_subreddit_12345") # Example of an invalid subreddit
    print("-" * 20)
    top_ten("AskReddit")