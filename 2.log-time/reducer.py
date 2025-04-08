import sys  # 컴퓨터가 입력을 받을 수 있도록 도와주는 도구를 불러와요

last_hour = None   # 전에 본 시간이 뭐였는지 기억해두는 변수 (처음엔 없음)
total_count = 0    # 그 시간에 몇 명이 있었는지 저장하는 변수

# 예시 입력 데이터:
# 03    1
# 03    1
# 04    1
# 05    1

# 한 줄씩 차례로 읽어요
for line in sys.stdin:
    line = line.strip()  # 줄 끝에 있는 줄바꿈이나 빈칸을 없애요

    hour, value = line.split()  # 한 줄을 나눠서 "시간"과 "사람 수"로 나눠요
    value = int(value)          # 사람 수를 숫자로 바꿔줘요 (예: "1" → 1)

    # 만약 이번 줄의 시간이 앞에서 본 시간이랑 같다면?
    if last_hour == hour:
        total_count += value  # 사람 수를 계속 더해줘요
    else:
        # 시간이 바뀌었을 때, 그 전 시간의 총 사람 수를 출력해요
        if last_hour is not None:
            print(f'{last_hour}\t{total_count}')  # 시간과 총 사람 수를 보여줘요

        # 그리고 새로운 시간으로 기억을 바꾸고, 사람 수도 새로 시작해요
        last_hour = hour
        total_count = value

# 마지막 시간에 대한 결과도 꼭 출력해줘야 해요!
print(f'{last_hour}\t{total_count}')