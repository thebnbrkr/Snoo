import praw

reddit = praw.Reddit(client_id='o-0moazmFjjWNA', client_secret = 'jap7ZhKDNpKMwxlAAUWv6DUTy3Hdkg', username ='rhcpbot', password ='###########', user_agent='007')

subreddit = reddit.subreddit('ubco')
hot = subreddit.hot(limit=3)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
   
for comment in subreddit.stream.comments():
	try:
		parent_id = str(comment.parent())
		
		original = reddit.comment(parent_id)
		print('Parent : ')
		print(original.body)
		print('Reply:')
		print(comment.body)
	except praw.exceptions.PRAWException as e:
		pass
