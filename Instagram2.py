import praw

reddit = praw.Reddit(client_id='1234567890', client_secret = 'qAWESRDTFGYHUJKL', username ='ASZDXFCGVHBJNKM,L', password ='###########', user_agent='007')

subreddit = reddit.subreddit('ubco')
hot = subreddit.hot(limit=3)
for submission in hot:
    print(submission.title)
    print(submission.ups)
    print(submission.downs)
    print(submission.visited)
   
comments = submission.comments.list()
for comment in comments:
	print(25*'bam')
	print("Parent id : ", comment.parent)
	print("Comment id : ", comment.id)
	print(comment.body)
#	if len(comment.replies) > 0:
#		for reply in comment.replies:
	#		print("Skrattar", reply.body)

	
