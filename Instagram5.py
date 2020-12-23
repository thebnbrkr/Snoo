import praw

reddit = praw.Reddit(client_id='AWZSEXDRCFTVGBHJNMKL,;', client_secret = 'AWZSEXDCRFVGBHJNMK,L', username ='AZSXDCFGVBHJNMK,L;.', password ='###########', user_agent='007')

subreddit = reddit.subreddit('ubco')
hot = subreddit.hot(limit=5)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
    
submission = reddit.submission(url="https://www.reddit.com/r/ubco/comments/k4621y/title/")
submission.reply('Cancun, Mexico')
