#!/usr/bin/env python

import sys

count_line = 0
firstline = True
for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    for word in words[24:30]:
        if len(word)>0 and not word.isdigit():
            print word + '              1'
