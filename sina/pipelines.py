# -*- coding: utf-8 -*-

import pymongo
from items import InformationItem,TweetsItem,FollowsItem,FansItem
from scrapy.exceptions import DropItem
from custom_crawler import settings

class MongoDBPipleline(object):
	def __init__(self,mongo_uri,mongo_db):
		client=pymongo.MongoClient(mongo_uri)
		db=client[mongo_db]
		self.Information=db["Information"]
		self.Tweets=db["Tweets"]
		self.Follows=db["Follows"]
		self.Fans=db["Fans"]

	@classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATA_BASE')
        )


	def process_item(self,item,spider):
		if isinstance(item,InformationItem):
			for data in item:
				if not data:
			 		raise DropItem("Missing data!")
			self.Information.update({'_id':item['_id']},dict(item),upsert=True)
		elif isinstance(item,TweetsItem):
			for data in item:
				if not data:
					raise DropItem("Missing data!")
			self.Tweets.update({'_id':item['_id']},dict(item),upsert=True)
		elif isinstance(item,FollowsItem):
			for data in item:
				if not data:
					raise DropItem("Missing data!")
			self.Follows.update({'_id':item['_id']},dict(item),upsert=True)
		elif isinstance(item,FansItem):
			for data in item:
				if not data:
					raise DropItem("Missing data!")
			self.Fans.update({'_id':item['_id']},dict(item),upsert=True)
		return item