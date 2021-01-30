# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
import os

class WebcrawlerPipeline:
    def __init__(self):
        self.file = open("my_news.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

        self.setupDBCon()
        # self.createTables()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        self.storeInDb(item)
        return item

    def setupDBCon(self):
        self.con = sqlite3.connect(os.path.abspath('C:/Users/user/Desktop/자연어처리과정/WebProject/InfoWeb/db.sqlite3')) #Change this to your own directory
        self.cur = self.con.cursor()
    
    # def createTables(self):
    #     self.cur.execute("DROP TABLE IF EXISTS news_list")

    #     self.cur.execute("CREATE TABLE IF NOT EXISTS news_list(id INTEGER PRIMARY KEY NOT NULL title TEXT, writer TEXT, article TEXT href TEXT \
    #     modify_date DATETIME)")
    
    def storeInDb(self,item):
        self.cur.execute("INSERT INTO news_list(slug, title, writer, article, href, modify_date) VALUES( ?, ?, ?,?,?,?)", ( \
        item.get('slug',''),
        item.get('title','').strip(),
        item.get('writer','').strip(),
        item.get('article','').strip(),
        item.get('href','').strip(),
        '2020/01/31',
        ))
        print('------------------------')
        print('Data Stored in Database')
        print('------------------------')
        self.con.commit()