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
pos_parsed = os.path.join(data_dir, 'positive_parsed.data')
pos_mat_path = os.path.join(data_dir, 'positive_mat.npy')
neg_raw = os.path.join(data_dir, 'negative_raw.data')
neg_json = os.path.join(data_dir, 'negative.data')
neg_parsed = os.path.join(data_dir, 'negative_parsed.data')
neg_mat_path = os.path.join(data_dir, 'negative_mat.npy')

words_path = os.path.join(data_dir, 'words.data')
mat_path = os.path.join(data_dir, 'mat.data')
mi_path = os.path.join(data_dir, 'mi.data')

token_path = os.path.join(data_dir, 'select_token_20161226.data')

pos_count = 2896
neg_count = 32338
vec_length = 250

total_count = pos_count + neg_count
