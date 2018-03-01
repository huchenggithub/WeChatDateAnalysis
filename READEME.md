#基于Python实现的微信好友数据分析
http://blog.csdn.net/qinyuanpei/article/details/79360703
基于 Python 对微信好友进行数据分析，这里选择的维度主要有：性别、头像、签名、位置，
主要采用图表和词云两种形式来呈现结果，其中，对文本类信息会采用词频分析和情感分析两种方法。
* itchat：微信网页版接口封装Python版本，在本文中用以获取微信好友信息。 
* jieba：结巴分词的 Python 版本，在本文中用以对文本信息进行分词处理。 
* matplotlib： Python 中图表绘制模块，在本文中用以绘制柱形图和饼图 
* snownlp：一个 Python 中的中文分词模块，在本文中用以对文本信息进行情感判断。 
* PIL： Python 中的图像处理模块，在本文中用以对图片进行处理。 
* numpy： Python中 的数值计算模块，在本文中配合 wordcloud 模块使用。 
* wordcloud： Python 中的词云模块，在本文中用以绘制词云图片。 
* TencentYoutuyun：腾讯优图提供的Python版本SDK，在本文中用以识别人脸及提取图片标签信息。 
>以上模块均可通过 pip 安装，关于各个模块使用的详细说明，请自行查阅各自文档。
