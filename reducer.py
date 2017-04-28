#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('          ')
    try:
        count = int(count)
    except Exception:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word and current_word != "VEHICLE TYPE CODE 1" and current_word != "VEHICLE TYPE CODE 2" and current_word != "VEHICLE TYPE CODE 3" and current_word != "VEHICLE TYPE CODE 4" and current_word != "VEHICLE TYPE CODE 5":
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word
