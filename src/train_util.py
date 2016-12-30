#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 28 Dec 2016 17:33:00
#
#

import tensorflow as tf
import numpy as np

from config import *

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def get_train_batch(n):
    n %= 100

    pos = np.load(pos_mat_path)[n * 25: n * 25 + 25, :]
    neg = np.load(neg_mat_path)[n * 300: n * 300 + 300, :]

    res = np.vstack((pos, neg))

    np.random.shuffle(res)

    return res[:, :-1], res[:, -1:]


def get_test_batch():
    pos = np.load(pos_mat_path)
    neg = np.load(neg_mat_path)

    res = np.vstack((pos[-396:, :], neg[-2338:, :]))

    np.random.shuffle(res)

    return res[:, :-1], res[:, -1:]

