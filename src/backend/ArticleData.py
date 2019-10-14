import requests
from bs4 import BeautifulSoup
from PttWebCrawler.crawler import *
import json
import pandas as pd

class QueryArticle():
    def __init__(self):
        self.title = ''
        self.aid = ''
        self.df = None
        self.postIP = ''
        self.postUid = ''
        self.msg_b = self.msg_n = self.msg_p = self.msg_a = 0
        self.push = ''
        
    # 取得文章代碼，沒找到return空字串
    def GetAid(self, title):
        gossipSearchLink = "https://www.ptt.cc/bbs/Gossiping/search?q="
        resp = requests.get(gossipSearchLink+title.replace(' ', ''),cookies={'over18': '1'})
        soup = BeautifulSoup(resp.text, 'html.parser')
        for result in soup.findAll("div", {"class": "title"}):
            if "Re:" not in result.findAll("a")[0].contents[0]:
                url = result.findAll("a")[0]['href']
                break
        if url:
            self.aid = url[url.find("M"):url.rfind(".")]   
            return
        
    # 使用ptt-web-crawler爬文章完整資訊
    def CrawlArticleInfo(self):
        aid = self.aid
        c = PttWebCrawler(as_lib=True)
        c.parse_article(aid, 'Gossiping')
        ## json format: Gossiping-"aid".json
        JsonFile = "Gossiping-{}.json".format(aid)
        
        with open(JsonFile) as infile:
            data = json.load(infile)
        self.df = pd.io.json.json_normalize(data)
        self.parsePushes()
        
    def MessageCount(self):
        self.msg_b = self.df['message_count.boo'][0]
        self.msg_n = self.df['message_count.neutral'][0]
        self.msg_p = self.df['message_count.push'][0]
        self.msg_a = self.df['message_count.all'][0]
        
    def UserInfo(self):
        self.postUid = self.df['author'][0]
        self.postIP = self.df['ip'][0]
        
    def parsePushes(self):
        push_before = self.df['messages'][0]
        push_after = []
        for i in range(len(push_before)):
            push_after.append(push_before[i]['push_content'])
        self.push = push_after