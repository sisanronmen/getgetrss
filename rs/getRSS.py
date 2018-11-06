import feedparser
import pandas as pd
import time
import datetime
import sqlite3



def main():
    $conn=sqlite3.connect(r"C:\Users\azco-virt-02\Desktop\sqlite-tools-win32-x86-3250200\test")
    #cursor=conn.cursor()
    #cursor.execute("insert into rssTbl values('日経新聞 速報','https://www.nikkei.com/news/category/','2018/11/5  1:51:00',0,1)")
    pds=getFeed()
    with sqlite3.connect(r"C:\Users\azco-virt-02\Desktop\sqlite-tools-win32-x86-3250200\test") as conn:
        pds.to_sql('rssTbl',conn,if_exists="replace")
        #pds.to_csv("test2.csv",encoding="shift_jis")
        conn.commit

def getFeed():
    lists=[]
    lists.append("https://assets.wor.jp/rss/rdf/nikkei/news.rdf")
    lists.append("https://assets.wor.jp/rss/rdf/nikkei/business.rdf")
    lists.append("https://assets.wor.jp/rss/rdf/nikkei/markets.rdf")
    lists.append("https://assets.wor.jp/rss/rdf/nikkei/technology.rdf")
    lists.append("https://assets.wor.jp/rss/rdf/reuters/stock.rdf")

    rssList = []
    for i,l in enumerate(lists):
        rss = feedparser.parse(l)
        rssList.append([rss.feed.title,rss.feed.link,"",i,"1"])
        #RSS情報をリストに格納
        for entry in rss.entries:
            #RSS情報をリストに格納
            rssList.append([entry.title,entry.link,time.strftime('%Y/%m/%d %X',entry.updated_parsed),i,"0"])

    #RSS情報をデータフレームに格納
    pds = pd.DataFrame(rssList)
    pds.columns = ["title","link","time","category","flag"]
    return pds

if __name__ == '__main__':
    main()
