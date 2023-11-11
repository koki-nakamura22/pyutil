from requests_oauthlib import OAuth1Session
import os
import json

# 事前に取得したアクセストークンとシークレットを環境変数に設定
os.environ['API_KEY'] = '実際の値'
os.environ['API_KEY_SECRET'] = '実際の値'
os.environ['ACCESS_TOKEN'] = '実際の値'
os.environ['ACCESS_TOKEN_SECRET'] = '実際の値'

consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

# ツイートの内容を設定
payload = {"text": "Hello world!"}

# OAuth1セッションを設定
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Twitterのツイートポストエンドポイント
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

# レスポンスの確認
if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
