#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Thu 22 Dec 2016 19:56:32
#
#

from config import *

import json
import pickle
import codecs
import jieba as jb

encode = 'utf-8'

words_file = codecs.open(words_path, 'r', encode)

words = {word.strip(): [0, 0] for word in words_file.readlines()}


pos_file = codecs.open(pos_json, 'r', encode)
neg_file = codecs.open(neg_json, 'r', encode)

for pos in pos_file.readlines():
    obj = json.loads(pos)
    ws = set(jb.cut(obj['data']))
    for w in ws:
        w = w.strip()
        if w != '':
            words[w][0] += 1

for neg in neg_file.readlines():
    obj = json.loads(neg)
    ws = set(jb.cut(obj['data']))
    for w in ws:
        w = w.strip()
        if w != '':
            words[w][1] += 1

f = open(mat_path, 'wb')
pickle.dump(words, f, pickle.HIGHEST_PROTOCOL)

f.close()
pos_file.close()
neg_file.close()
words_file.close()

