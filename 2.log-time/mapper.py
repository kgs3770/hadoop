import sys  # 컴퓨터한테 "입력 받는 도구"를 쓰게 해주는 코드야

# 처음에는 아무 영화도 없고, 점수도 없고, 개수도 0개야!
currunt_movie_id = None   # 지금 보고 있는 영화 번호 (처음엔 없음)
currunt_sum = 0           # 지금까지 받은 점수 합계
currunt_count = 0         # 지금까지 받은 점수 개수

# 컴퓨터가 한 줄씩 읽으면서 반복해
for line in sys.stdin:
    line = line.strip()  # 줄 끝에 붙은 줄바꿈이나 공백을 없애줘
    movie_id, rating = line.split()  # 줄을 나눠서 영화 번호와 점수로 나눠줘

    try:
        rating = float(rating)  # 점수를 숫자로 바꿔줘 (예: "5.0" → 5.0)
    except:
        continue  # 숫자로 못 바꾸면 그 줄은 무시하고 넘어가

    # 만약 이번 영화가 우리가 지금까지 보고 있던 영화랑 같다면?
    if currunt_movie_id == movie_id:
        currunt_count += 1      # 점수 개수 하나 더 늘려줘
        currunt_sum += rating   # 점수를 합계에 더해줘
    else:
        # 영화가 바뀌었어! 그럼 지금까지 계산한 평균 점수를 출력해야 해
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum / currunt_count  # 평균 점수 = 총합 ÷ 개수
            print(f'{currunt_movie_id}\t{currunt_avg}')  # 영화 번호랑 평균 점수를 보여줘

        # 이제 새로운 영화니까 다시 시작해야 해!
        currunt_movie_id = movie_id  # 새로운 영화 번호로 바꿔줘
        currunt_count = 1            # 점수 개수 1개부터 시작
        currunt_sum = rating         # 점수 합계도 새 점수로 시작

# 마지막 영화도 출력해야 해! (반복문 끝났을 때)
currunt_avg = currunt_sum / currunt_count  # 마지막 영화의 평균 계산
print(f'{currunt_movie_id}\t{currunt_avg}')  # 마지막 영화의 평균 점수도 출력