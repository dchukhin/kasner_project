import twitter

api = twitter.Api(
    consumer_key = '',
    consumer_secret = '',
    access_token_key = '',
    access_token_secret = ''
    )


search1='kasner_search'
search = api.GetSearch(term=search1, lang='en', count=10)
for tweet in search:
    user_name = tweet.user.screen_name 
    created_at = tweet.created_at
    text =  tweet.text
