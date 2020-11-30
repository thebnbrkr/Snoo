import praw

reddit = praw.Reddit(client_id='o-0moazmFjjWNA', client_secret = 'jap7ZhKDNpKMwxlAAUWv6DUTy3Hdkg', username ='rhcpbot', password ='Reddit@9846099857', user_agent='007')

subreddit = reddit.subreddit('python')
hot = subreddit.hot(limit=5)
for submission in hot:
    print(submission)