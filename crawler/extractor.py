import pandas as pd
import praw
from praw.models import MoreComments

#use praw.ini file to initialize reddit object
#reddit = praw.Reddit("bot1", user_agent="bot1 user agent")
reddit = praw.Reddit(
    client_id="_Z-UctTbLwJV10tOmCuMng",
    client_secret="-pvmI9ANIJxLXUA8Ue3t_Hq2GvvlUw",
    user_agent="bot1")

#testing that it is the correct user
print(f"current user: {reddit.user.me()}")

#reddit url
#url = "https://www.reddit.com/r/UpliftingNews/comments/lemy1b/student_who_made_30k_from_gamestop_donates_games/"
#submission = reddit.submission(url=url)

'''
    table = []
    reply = []
    submission.comments.replace_more(limit=None) #replace all MoreComments objects with the actuall comments
    for sub in list(reddit.subreddit("wallstreetbets").top("all"))[:5]:
        posts = []
        #for top_level_comment in sub.comments.list(): #gets the subcomments of comments in a hierarchical order(First iterate subcomments then next comment)
        for top_level_comment in sub.comments[1:6]:
            if isinstance(top_level_comment, MoreComments) or top_level_comment.author == None:
                continue
            #posts.append(top_level_comment.body) #get comment's body
            for r in top_level_comment.replies:
                if isinstance(r, MoreComments):
                    continue
                reply.append(r.body)
            posts.append(top_level_comment.author.name) #get comment's redditor name 
        table.append(posts)
    posts = pd.DataFrame(table,columns=[str(i+1) for i in range(5)])
    print(posts)
    print(reply)
'''

users = []
for sub in list(reddit.subreddit("wallstreetbets").top("all"))[:1]:
    '''
    comments = sub.comments
    while isinstance(comments[-1], MoreComments):
        print(list(comments), "---------->1\n")
        print(f"Replacing with {comments[-1].comments()}\n")
        comments = comments[:-1] + comments[-1].comments()
        print(list(comments), "---------->2\n")
    '''
        
    #comments = [comment.comments() if isinstance(comment, MoreComments) else comment for comment in comments]
    #final_comments = []
    #comments = [comment.comments() if isinstance(comment, MoreComments) else comment for comment in comments]
    #limit = len(comments)
    #for i in range(limit):
        #if isinstance(comments[i], MoreComments):
            #comments[i] = comments[]
    sub.comments.replace_more(limit=None)
    for top_level_comment in sub.comments:
        if top_level_comment.author == None:
            continue
        if top_level_comment.author.name not in users:
            users.append(top_level_comment.author.name) #get comment's redditor name 
#users = pd.DataFrame(users,columns=["users of first post"])
print(users)

