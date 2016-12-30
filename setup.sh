#!/bin/bash
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Fri 30 Dec 2016 15:17:19
#
#

# setup 3rd party
cd ./lib/3rd/
git clone https://github.com/fxsjy/jieba.git
cd ../../

# data folder
mkdir data

# create model folder
mkdir model
cd model
mkdir tf
cd ..
