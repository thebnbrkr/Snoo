import praw

reddit = praw.Reddit(client_id='o-0moazmFjjWNA', client_secret = 'jap7ZhKDNpKMwxlAAUWv6DUTy3Hdkg', username ='rhcpbot', password ='###########', user_agent='007')

subreddit = reddit.subreddit('kelowna')
hot = subreddit.hot(limit=5)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
    
subreddit.unsubscribe()
