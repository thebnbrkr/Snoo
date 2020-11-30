import praw

reddit = praw.Reddit(client_id='o-0moazmFjjWNA', client_secret = 'jap7ZhKDNpKMwxlAAUWv6DUTy3Hdkg', username ='rhcpbot', password ='Reddit@9846099857', user_agent='007')

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
