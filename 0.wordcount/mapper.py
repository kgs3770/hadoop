#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip() #strip=공백제거
    words = line.split() #각각의 단어로 데이터 나눔

    for word in words:
        print(f'{word}\t1')
    # cat text.txt | python3 mapper.py 

    