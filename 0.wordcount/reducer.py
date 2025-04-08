#!/usr/bin/env python3  # 이 파일이 파이썬3로 실행된다는 뜻이에요!

import sys  # 입력을 받을 수 있도록 도와주는 도구예요

# 예시 입력 (단어와 숫자):
# apple    1
# apple    1
# hello    1
# ...

last_word = None   # 전에 본 단어를 기억하는 변수 (처음엔 아무것도 없음)
total_count = 0    # 그 단어가 몇 번 나왔는지 저장하는 변수

# 한 줄씩 읽어요!
for line in sys.stdin:
    word, value = line.split('\t')  # 줄을 탭(\t)으로 나눠서 단어와 숫자로 나눠요
    value = int(value)              # 숫자 모양의 글자를 진짜 숫자로 바꿔요 (예: "1" → 1)

    # 만약 지금 단어가 전과 같다면?
    if last_word == word:
        total_count += value  # 개수를 계속 더해줘요
    else:
        # 단어가 바뀌었으면, 전에 봤던 단어의 총 개수를 출력해요!
        if last_word is not None:
            print(f'{last_word}\t{total_count}')  # 예: apple    2

        # 이제 새 단어로 바꾸고, 개수도 새로 시작해요
        last_word = word
        total_count = value  # 처음 나온 거니까 1부터 시작!

# 마지막 단어도 출력해줘야 해요!
if last_word == word:
    print(f'{last_word}\t{total_count}')

# cat text.txt | python3 mapper.py | sort
# 데이터 어디서, 저장 어디, 