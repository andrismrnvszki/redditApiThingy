from bs4 import BeautifulSoup
import requests, redvid


def downloadAll(list):
    counterP = 1
    for i in list:
        
        #print(i)
        headers = ""
        if "v.redd.it" in i:
            print("No.:",counterP)
            counterP+=1
            reddit = redvid.Downloader(max_q=True)
            print(i)
            response = requests.get(i)
            if response.status_code == 200:
                reddit.url = i
                reddit.path = "C:/Users/marin/redditApiThingy/videos"
                reddit.download()
            else:
                print("Ez egy fákiii")
            
            

        if "gfycat.com/" in i:
            print("No.:",counterP)
            counterP+=1
            headers = {"Referer": "https://giant.gfycat.com/"}
            url = i
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            for v in soup.select("video source[src]"):
                if "mobile" not in v["src"].split("/")[-1].strip():
                    print("Downloading {}".format(v["src"]))
                    with open("videos/"+v["src"].split("/")[-1].strip(), "wb") as f_out:
                        f_out.write(requests.get(v["src"].strip(), headers=headers).content)
        
