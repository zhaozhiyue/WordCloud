import jieba #导入jieba分词库
from wordcloud import WordCloud#导入wordcloud库，用来生成词云
with open ("yitiantulongji.txt","r",encoding='utf-8') as f:
    txt=f.read()
#另一种打开文件的方式，比较麻烦，推荐使用第一种
# f=open("yitiantulongji.txt","r",encoding='utf-8')
# txt=f.read()
# f.close()
ls={'说道','甚么','自己','一个','咱们','心中','一声','只见','武功',\
    '便是','不是','如此','不知','弟子','之中','出来','如何','突然',\
        '突然','他们'}#排除一些无意义的词语，仅作为示例

words=jieba.lcut(txt)
newtxt=''.join(words)
wordcloud=WordCloud(background_color="white",width=800,font_path='./fonts/simhei.ttf',\
    stopwords=ls,height=600,max_words=200,max_font_size=80).generate(newtxt)
wordcloud.to_file('倚天屠龙记基本词云.png')