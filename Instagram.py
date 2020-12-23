import praw

reddit = praw.Reddit(client_id='1234567890', client_secret = '234567890-', username ='1234567890-', password ='###########', user_agent='007')

subreddit = reddit.subreddit('kelowna')
hot = subreddit.hot(limit=5)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
    
subreddit.unsubscribe()
