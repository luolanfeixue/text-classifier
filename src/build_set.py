#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Mon 26 Dec 2016 15:55:52
#
#

from config import *

import numpy as np
import codecs as cc
import json

encode = 'utf-8'

pos = cc.open(pos_parsed, 'r', encode)
neg = cc.open(neg_parsed, 'r', encode)

token = cc.open(token_path, 'r', encode)

tokens = {}

token_id = 0
for line in token:
    word = line.strip().split(',')[0]
    tokens.setdefault(word, token_id)
    token_id += 1

def build_mat(count, file):
    mat = np.zeros((count, vec_length), dtype=np.float32)

    id = 0
    for line in pos.readlines():
        text = line.split()
        for word in text:
            word = word.strip()
            if tokens.has_key(word):
                mat[id][tokens[word]] = 1
        id += 1

    return mat

pos_mat = build_mat(pos_count, pos)
neg_mat = build_mat(neg_count, neg)

np.save(pos_mat_path, pos_mat)
np.save(neg_mat_path, neg_mat)

pos.close()
neg.close()
