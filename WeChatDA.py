#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Newton_apple time:2018-03-01

import matplotlib.pyplot as plt
import itchat
'''collections模块自Python 2.4版本开始被引入，包含了dict、set、list、tuple以外的一些特殊的容器类型
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，
以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。'''
from collections import Counter

'''
使用itchat模块获取微信好友信息
同平时登录网页版微信一样，我们使用手机扫描二维码就可以登录，这里返回的friends对象是一个集合，第一个元素是当前用户。
所以，在下面的数据分析流程中，我们始终取friends[1:]作为原始输入数据，集合中的每一个元素都是一个字典结构，
以我本人为例，可以注意到这里有Sex、City、Province、HeadImgUrl、Signature这四个字段

Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
Login successfully as 兔呆呆
<class 'itchat.storage.templates.ContactList'>

[<User: {'MemberList': <ContactList: []>, 
'UserName': '@4ceea222ffbc7a3cfba7eaae8242df5edc35a0c2ed53298861be19373bc63682', 
'City': '', 'DisplayName': '', 'PYQuanPin': '', 'RemarkPYInitial': '', 'Province': '', 
'KeyWord': '', 'RemarkName': '', 'PYInitial': '', 'EncryChatRoomId': '', 'Alias': '', 
'Signature': '苦难显才华，好运隐天资', 'NickName': '兔呆呆', 'RemarkPYQuanPin': '', 
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=654388938&username=@4ceea222ffbc7a3cfba7eaae8242df5edc35a0c2ed53298861be19373bc63682&skey=@crypt_bb9141de_437bcba29aaf77daf711ac183ad89fc4', 
'UniFriend': 0, 'Sex': 2, 'AppAccountFlag': 0, 'VerifyFlag': 0, 'ChatRoomId': 0, 
'HideInputBarFlag': 0, 'AttrStatus': 0, 'SnsFlag': 1, 'MemberCount': 0, 'OwnerUin': 0, 
'ContactFlag': 0, 'Uin': 1157494577, 'StarFriend': 0, 'Statues': 0, 'WebWxPluginSwitch': 0, 
'HeadImgFlag': 1}>, 

<User: {'MemberList': <ContactList: []>, 'Uin': 0, 
'UserName': '@4e4e5cdc49cf9ebe045e5d101f24345f', 'NickName': 'Sven', 
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=647683172&username=@4e4e5cdc49cf9ebe045e5d101f24345f&skey=@crypt_bb9141de_437bcba29aaf77daf711ac183ad89fc4', 
'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 1, 
'Signature': '酒不自醉人自醉，宽衣解带终不悔', 'VerifyFlag': 0, 'OwnerUin': 0, 
'PYInitial': 'SVEN', 'PYQuanPin': 'Sven', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 
'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 208935, 'Province': '北京', 
'City': '', 'Alias': '', 'SnsFlag': 17, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 
'KeyWord': 'huc', 'EncryChatRoomId': '', 'IsOwner': 0}>, 

<User: {'MemberList': <ContactList: []>, 
'Uin': 0, 'UserName': '@9cf6154d838e728a9245b12cb5fb7dc9', 'NickName': 'King', 
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=659490427&username=@9cf6154d838e728a9245b12cb5fb7dc9&skey=@crypt_bb9141de_437bcba29aaf77daf711ac183ad89fc4', 'ContactFlag': 3, 'MemberCount': 0, 
'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '我在茫茫人海中访寻我人生之唯一伴侣，得知我幸，失之我命...', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'KING', 
'PYQuanPin': 'King', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 
'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4307047, 'Province': '四川', 'City': '成都', 
'Alias': '', 'SnsFlag': 17, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': 'kin', 
'EncryChatRoomId': '', 'IsOwner': 0}>]

'''
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)

def analyse_sex(friends):
	"""分析好友性别，我们首先要获得所有好友的性别信息，这里我们将每一个好友信息的Sex字段提取出来，
	然后分别统计出Male、Female和Unkonw的数目，我们将这三个数值组装到一个列表中，
	即可使用matplotlib模块绘制出饼图来"""

	# 提取Sex字段组成sexs列表, map()会根据提供的函数对指定序列做映射
	sexs = list(map(lambda x: x['Sex'], friends[1:]))

	counts = list(map(lambda x: x[1], Counter(sexs).items()))
	labels = [u'性别不明', u'男性', u'女性']
	colors = ['red', 'yellowgreen', 'lightskyblue']
	plt.figure(figsize=(8,5), dpi=80)
	plt.axes(aspect=1)
	plt.pie(counts,  # 性别统计结果
	        labels=labels,  # 性别展示标签
	        colors=colors,  # 饼图区域配色
	        labeldistance=1.1,  # 标签距离圆点距离
	        autopct='%3.1f%%',  # 饼图区域文本格式
	        shadow=False,  # 饼图是否显示阴影
	        startangle=90,  # 饼图起始角度
	        pctdistance=0.6  # 饼图区域文本距离圆点距离
	        )
	plt.legend(loc='upper right', )
	plt.title(u'%s的微信好友性别组成' % friends[0]['NickName'])
	plt.show()


analyse_sex(friends)

