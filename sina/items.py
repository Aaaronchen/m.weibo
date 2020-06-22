# -*- coding: utf-8 -*-
import scrapy

from scrapy import Item,Field

class InformationItem(Item):
	_id=Field() #用户ID
	NickName=Field() #昵称
	Gender=Field() #性别
	Signature=Field() #个性签名
	Num_Tweets=Field() #微博数
	Num_Follows=Field() #关注数
	Num_Fans=FiField() #粉丝数eld() #粉丝数
	Pic=Field() #头像
	Verified=Field() #认证

class TweetsItem(Item):
	_id=Field() #微博ID
	ID=Field() #用户ID
	Content=Field() #微博内容
	PubTime=Field() #发表时间
	Like=Field() #点赞数
	Comment=Field() #评论数
	Transfer=Field() #转载数
	Scheme=Field() #来源地址

class FollowsItem(Item):
	_id=Field() #好友ID
	ID=Field() #用户ID
	NickName=Field() #昵称
	Signature=Field() #个性签名
	Num_Tweets=Field() #微博数
	Num_Follows=Field() #关注数
	Num_Fans=Field() #粉丝数
	profile_url=Field() #主页链接
	

class FansItem(Item):
	_id=Field() #粉丝ID
	ID=Field() #用户ID
	NickName=Field() #昵称
	Signature=Field() #个性签名
	Num_Tweets=Field() #微博数
	Num_Follows=Field() #关注数
	Num_Fans=Field() #粉丝数
	profile_url=Field() #主页链接
	