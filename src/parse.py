#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 20 Dec 2016 19:50:21
#
#
import codecs
import json
import re
import base64

from config import *
import jieba as jb

pattern = re.compile(r'\s+')

encode = 'utf-8'

pos_file = codecs.open(pos_json, 'r', encode)
neg_file = codecs.open(neg_json, 'r', encode)
pos_parsed_file = codecs.open(pos_parsed, 'w', encode)
neg_parsed_file = codecs.open(neg_parsed, 'w', encode)

words = set()

for line in pos_file.readlines():
    obj = json.loads(line)
    pos_set = set(jb.cut(pattern.sub(' ', obj['data'])))
    words |= pos_set
    pos_parsed_file.write(base64.b64encode(' '.join(pos_set).encode(encode)) + '\n')

for line in neg_file.readlines():
    obj = json.loads(line)
    neg_set = set(jb.cut(pattern.sub(' ', obj['data'])))
    words |= neg_set
    neg_parsed_file.write(base64.b64encode(' '.join(neg_set).encode(encode)) + '\n')

words_file = codecs.open(words_path, 'w', encode)
for word in words:
    words_file.write(word.strip() + '\n')

pos_file.close()
neg_file.close()
words_file.close()
