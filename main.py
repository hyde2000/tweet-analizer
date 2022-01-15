import os
import json

from requests import request

bearer_token = os.getenv("BEARER_TOKEN")


def create_url() -> str:
    tweet_fields = "tweet.fields=lang,author_id"
    ids = "ids=1278747501642657792,1255542774432063488"
    url = f"https://api.twitter.com/2/tweets?{ids}&{tweet_fields}"

    return url


def bearer_auth(req):
    req.headers["Authorization"] = f"Bearer {bearer_token}"
    req.headers["User-Agent"] = "v2TweetLookupPython"

    return req


def request_to_endpoint(url: str):
    res = request("GET", url=url, auth=bearer_auth)
    print(res.status_code)

    if res.status_code != 200:
        raise Exception(f'Request Error: {res.status_code} {res.text}')

    return res.json()


def main():
    url = create_url()
    response = request_to_endpoint(url)
    print(json.dumps(response, indent=2, sort_keys=True))


main()
