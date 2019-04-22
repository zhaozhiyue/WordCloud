import jieba#导入jieba分词库
with open ("yitiantulongji.txt","r",encoding='utf-8') as f:#打开txt文件
    txt=f.read()#读取到变量txt中
ls={'说道','甚么','自己','一个','咱们','心中','一声','只见','武功','便是',\
    '不是','如此','不知','弟子','之中','出来','如何','师父','突然','突然',\
        '他们','教主'}#排除不想要的词语

words=jieba.lcut(txt)#用jieba中的lcut方法进行分词，存入words中
counts={}#新建一个空字典
for x in words:#用循环统计各各出现的个数，词语为字典的key，次数为value
    if len(x) ==1:
        continue
    elif x in ls:
        continue
    else:
        counts[x]=counts.get(x,0)+1

items=list(counts.items())#把字典转换为列表
items.sort(key=lambda x:x[1],reverse= True)#排序
for i in range(30):#打印出前30名的词语
    word, count=items[i]
    print(word,count)