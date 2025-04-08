#!/usr/bin/env python3

import sys

# apple 1
# apple 1
# hello 1
# ...



last_word = None
total_count = 0

for line in sys.stdin:
    word, value = line.split('\t') #\t을 기준으로 분리
    value = int(value)

    if last_word == word:
        total_count += value
        pass
    else:
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        last_word = word
        total_count = value #단어가 바뀌면 1부터 시작

if last_word == word:
    print(f'{last_word}\t{total_count}')

# cat text.txt | python3 mapper.py | sort
# 데이터 어디서, 저장 어디, 