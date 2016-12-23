#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 20 Dec 2016 19:50:21
#
#
import codecs
import json

from config import *
import jieba as jb

encode = 'utf-8'

pos_file = codecs.open(pos_json, 'r', encode)
neg_file = codecs.open(neg_json, 'r', encode)

words = set()

for line in pos_file.readlines():
    obj = json.loads(line)
    words |= set(jb.cut(obj['data']))

for line in neg_file.readlines():
    obj = json.loads(line)
    words |= set(jb.cut(obj['data']))

words_file = codecs.open(words_path, 'w', encode)
for word in words:
    words_file.write(word.strip() + '\n')

pos_file.close()
neg_file.close()
words_file.close()
