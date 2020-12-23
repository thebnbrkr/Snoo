import praw

reddit = praw.Reddit(client_id='QAWSEXDRCFTVGBHJNMK,L;.', client_secret = 'ZWESXDRCTFVGBHJNKML', username ='SXDCFGVBHJNKM', password ='###########', user_agent='007')

subreddit = reddit.subreddit('ubco')
hot = subreddit.hot(limit=3)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
   
for submission in subreddit.stream.submissions():
	try:
		print(submission.title)
	except Exception as e:
		print(str(e))
