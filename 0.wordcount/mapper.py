#!/usr/bin/env python3  # 이 파일이 파이썬3로 실행된다는 뜻이에요!

import sys  # 컴퓨터가 입력한 내용을 읽게 도와주는 도구예요

# 컴퓨터가 한 줄씩 글을 읽어요
for line in sys.stdin:
    line = line.strip()  # 줄 앞뒤에 있는 공백(띄어쓰기, 줄바꿈 등)을 없애요
    words = line.split()  # 문장을 띄어쓰기 기준으로 단어로 나눠요

    # 단어 하나씩 꺼내면서
    for word in words:
        print(f'{word}\t1')  # "이 단어는 1번 나왔어요!" 하고 출력해요
    # cat text.txt | python3 mapper.py 

    