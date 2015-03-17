#!/usr/bin/python
#coding:utf-8
# 功能: 在references.in中找出在sub.list中列出的文献, 并写入references.out
# 周吕文: zhou.lv.wen@gmail.com
import StringIO,re


# 输出文件
out= open("references.out","a+")

# 待筛选文件
data=open('references.in').readlines()
Jour= ([x[0:-1] for x in  data if re.search(r'Alternate Journal:',x)]);
njou=len(Jour)
full=open('references.in').read().split('\n\n');

# 列表文件
data=open('sub.list').readlines()
subs= ([x[0:-1] for x in  data]);
nsub=len(subs)
for j in range(njou):
    for s in range(nsub):
        if Jour[j][19:].lower()==subs[s].lower():
           print "%s\n" %(full[j])
           out.write(full[j]+"\n\n")
