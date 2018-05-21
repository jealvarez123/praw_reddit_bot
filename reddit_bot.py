import praw

reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username = '',
                     password = '',
                     user_agent = '')

subreddit = reddit.subreddit('aww')

hot_aww = subreddit.hot(limit=5)

for submission in hot_aww:
    if not submission,stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title, submission.ups, submission.downs, submission.visited))
