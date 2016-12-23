#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 23 Dec 2016 14:50:48
#
#

from __future__ import division
from config import *

import math
import pickle as pkl

words_file = open(mat_path, 'rb')
words = pkl.load(words_file)
words_file.close()

eps = 0

def calc_IM(pos0, pos1, neg0, neg1):
    e = 0.
    if math.fabs(pos0) > 1e-6: e += pos0 * math.log(pos0 / ((pos0 + pos1) * (pos0 + neg0) + eps))
    if math.fabs(pos1) > 1e-6: e += pos1 * math.log(pos1 / ((pos1 + pos0) * (pos1 + neg1) + eps))
    if math.fabs(neg0) > 1e-6: e += neg0 * math.log(neg0 / ((neg0 + neg1) * (neg0 + pos0) + eps))
    if math.fabs(neg1) > 1e-6: e += neg1 * math.log(neg1 / ((neg1 + neg0) * (neg1 + pos1) + eps))
    return e

print calc_IM(0.5, 0., 0.5, 0.)
print calc_IM(0.25, 0.25, 0.25, 0.25)
print calc_IM(.5, 0., 0., 0.5)

word_im = []
    
for word, counts in words.iteritems():
    pos1 = counts[0]
    neg1 = counts[1]
    pos0 = pos_count - pos1
    neg0 = neg_count - neg1

    im = calc_IM(pos0 / total_count, pos1 / total_count, neg0 / total_count, neg1 / total_count)

    word_im.append((word, im))
    
word_im.sort(key = lambda x: x[1])

for w in word_im[-100: ]:
    print w[0], w[1]
