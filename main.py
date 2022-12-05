import pandas as pd
from moviepy.editor import VideoFileClip, concatenate_videoclips
import login_data, helper, gatherURLs, download_videos
 

helper.cleanVideosFolder()

subreddits_a = ["WhyWomenLiveLonger", "shitposting"]
#subreddits_a = ["Eyebleach"]
reddit_read_only = login_data.reddit_read_only

top_posts = pd.DataFrame()

for subs in subreddits_a:
    top_posts = pd.concat([top_posts, gatherURLs.getURLsPD(subreddit=subs, limit=5)], ignore_index=True)


goodURLs = []

print(top_posts["Post URL"])

download_videos.downloadAll(top_posts["Post URL"])

onlyfiles = helper.printVideos()

maxW=0
maxH=0
onlyClips=[]
for i in range(len(onlyfiles)):
    if "240" not in onlyfiles[i] or "360" not in onlyfiles[i] or"480" not in onlyfiles[i]:# or "480" in onlyfiles[i]:
        v = VideoFileClip(onlyfiles[i])
        onlyClips.append(v)

print('-------------------')
#print(onlyClips)
print("Thats:",len(onlyClips))
print('-------------------')

    

final_clip=concatenate_videoclips(onlyClips, method="compose")
final_clip
final_clip.write_videofile("finalBeauty.mp4")
