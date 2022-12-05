import pandas as pd
import login_data

def getURLsPD(subreddit, time="week", reddit_read_only=login_data.reddit_read_only , limit=10) -> pd.DataFrame:
    output = pd.DataFrame()
    
    subreddit = reddit_read_only.subreddit(subreddit)
    posts = subreddit.top(time, limit=limit)
    posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
    for post in posts:
        posts_dict["Title"].append(post.title)
        posts_dict["Post Text"].append(post.selftext)
        posts_dict["ID"].append(post.id)            
        posts_dict["Score"].append(post.score)
        posts_dict["Total Comments"].append(post.num_comments)
        posts_dict["Post URL"].append(post.url)
    top_posts = pd.DataFrame(posts_dict)
    output=pd.concat([output, top_posts], ignore_index=True)
        
    return output


#top_posts=getURLsPD("Eyebleach")

#print(top_posts)

