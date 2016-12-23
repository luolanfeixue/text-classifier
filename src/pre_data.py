#coding=utf-8
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Tue 20 Dec 2016 17:29:12
#
#

import codecs
import re
import json

from config import *

encode = 'utf-8'

msgs_pattern = re.compile(r'\[.*\]')

def transform(input_file, output_file, label):
    fin = codecs.open(input_file, 'r', encode)
    fout = codecs.open(output_file, 'w', encode)

    head = fin.readline()

    for line in fin.readlines():
        msgs_text = msgs_pattern.search(line).group().replace('\\\\', '\\')
        msgs = json.loads(msgs_text)

        text = ' '.join(msg.get('body', '') for msg in msgs)

        fout.write(json.dumps({"data": text, "label": label}) + '\n')

    fin.close()
    fout.close()

transform(pos_raw, pos_json, 1)
transform(neg_raw, neg_json, 0)
