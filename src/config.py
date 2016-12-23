#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 20 Dec 2016 19:56:48
#
#
import sys
import os

# 3rd party
sys.path.append('../lib/3rd/jieba')


data_dir = '../data'

pos_raw = os.path.join(data_dir, 'positive_raw.data')
pos_json = os.path.join(data_dir, 'positive.data')
neg_raw = os.path.join(data_dir, 'negative_raw.data')
neg_json = os.path.join(data_dir, 'negative.data')

words_path = os.path.join(data_dir, 'words.data')

mat_path = os.path.join(data_dir, 'mat.data')

pos_count = 2896
neg_count = 32338

total_count = pos_count + neg_count
