#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 28 Dec 2016 17:22:20
#
#

import tensorflow as tf
import numpy as np
import datetime
import sklearn.metrics as skmt

from config import *
import train_util as tu

seed = 0

x = tf.placeholder(tf.float32, shape=[None, vec_length])
y_ = tf.placeholder(tf.float32, shape=[None, 1])

W1 = tu.weight_variable([vec_length, 100])
b1 = tu.weight_variable([100])
y1 = tf.matmul(x, W1) + b1
h1 = tf.nn.relu(y1)
keep_prob = tf.placeholder(tf.float32)
h1_drop = tf.nn.dropout(h1, keep_prob)

W_fc = tu.weight_variable([100, 1])
b_fc = tu.weight_variable([1])
y_nn = tf.matmul(h1_drop, W_fc) + b_fc

loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(y_nn, y_))
train_step = tf.train.AdadeltaOptimizer(1e-3).minimize(loss)

y_sig = tf.sigmoid(y_nn)
pred = tf.greater(y_sig, 0.5)
correct_pred = tf.equal(tf.cast(pred, tf.float32), y_)
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

sess = tf.InteractiveSession()
saver = tf.train.Saver()

saver.restore(sess, '../model/tf/2016-12-29 16:48:28.257796-10000.ckpt')

test_batch = tu.get_test_batch()

y_true = test_batch[1]

y_pred = pred.eval(feed_dict={
    x: test_batch[0], y_: test_batch[1], keep_prob: 1.0})

print 'recall %f' % skmt.recall_score(y_true, y_pred)
print 'precision %f' % skmt.precision_score(y_true, y_pred)
print 'f1 score %f' % skmt.f1_score(y_true, y_pred)
