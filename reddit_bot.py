import praw

reddit = praw.Reddit(client_id = '5ymneRklqpWMLg',
                     client_secret = '	YXa1oftVLuPRwnmKr2aIjG12GwY',
                     username = 'awwbot',
                     password = 'prawbot2779',
                     user_agent = 'awwbotv1')

subreddit = reddit.subreddit('aww')

hot_aww = subreddit.hot(limit=5)

for submission in hot_aww:
    if not submission,stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
