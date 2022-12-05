from os import listdir, remove
from os.path import isfile, join

def cleanVideosFolder():
    onlyfiles = [f for f in listdir("videos") if isfile(join("videos", f))]
    for i in onlyfiles:
        remove("videos/"+i)

def printVideos() -> list:
    onlyfiles = [f for f in listdir("videos") if isfile(join("videos", f))]
    print('-------------------')
    print(onlyfiles)
    print('-------------------')
    if "redvid_temp" in onlyfiles:
        remove("videos/redvid_temp")

    for i in range(len(onlyfiles)):
        onlyfiles[i]="videos/"+onlyfiles[i]
        
    return onlyfiles