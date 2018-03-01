#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Newton_apple time:2018-03-01

import itchat


'''
使用itchat模块获取微信好友信息
同平时登录网页版微信一样，我们使用手机扫描二维码就可以登录，这里返回的friends对象是一个集合，第一个元素是当前用户。
所以，在下面的数据分析流程中，我们始终取friends[1:]作为原始输入数据，集合中的每一个元素都是一个字典结构，
以我本人为例，可以注意到这里有Sex、City、Province、HeadImgUrl、Signature这四个字段，我们下面的分析就从这四个字段入手：
'''
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
