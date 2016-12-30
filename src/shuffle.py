#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 28 Dec 2016 20:30:43
#
#

import numpy as np

from config import *

pos = np.load(pos_mat_path)
neg = np.load(neg_mat_path)

np.random.shuffle(pos)
np.random.shuffle(neg)

np.save(pos_mat_path, pos)
np.save(neg_mat_path, neg)
