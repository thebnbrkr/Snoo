import praw

reddit = praw.Reddit(client_id='AWZSXDCFGVBHJNKML,', client_secret = 'SZXDCFGVBHJNMK,L', username ='ZSDXCF GVBHJNMK,L', password ='###########', user_agent='007')

subreddit = reddit.subreddit('ubco')
hot = subreddit.hot(limit=5)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
    
submission = reddit.submission(url="https://www.reddit.com/r/ubco/comments/k4621y/title/")
submission.reply('Mission successful')
submission.delete()
