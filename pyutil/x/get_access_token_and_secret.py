from requests_oauthlib import OAuth1Session
import os

def get_access_token_and_secret(api_key, api_key_secret):
    # OAuthセッションを開始
    oauth = OAuth1Session(api_key, client_secret=api_key_secret)

    # リクエストトークンの取得
    request_token_url = "https://api.twitter.com/oauth/request_token"
    fetch_response = oauth.fetch_request_token(request_token_url)

    oauth_token = fetch_response.get('oauth_token')
    oauth_verifier = fetch_response.get('oauth_token_secret')

    # アクセストークンの交換を行う
    oauth = OAuth1Session(api_key, client_secret=api_key_secret, resource_owner_key=oauth_token, verifier=oauth_verifier)
    access_token_url = "https://api.twitter.com/oauth/access_token"

    # アクセストークンとシークレットの取得
    oauth_tokens = oauth.fetch_access_token(access_token_url)
    access_token = oauth_tokens.get('oauth_token')
    access_token_secret = oauth_tokens.get('oauth_token_secret')

    return access_token, access_token_secret

def main():
    access_token, access_token_secret = get_access_token_and_secret(
        os.environ.get("API_KEY"),
        os.environ.get("API_KEY_SECRET")
    )
    # 取得したアクセストークンとシークレットを出力
    print("Access Token:", access_token)
    print("Access Token Secret:", access_token_secret)

if __name__ == '__main__':
    main()
