import sys  # 표준 입력을 받기 위해 sys 모듈 사용

# 변수 초기화
currunt_movie_id = None  # 현재 처리 중인 영화 ID (오타 있음: "currunt" → "current"가 맞지만 유지함)
currunt_sum = 0          # 현재 영화의 평점 총합
currunt_count = 0        # 현재 영화에 대한 평점 수

# 표준 입력을 한 줄씩 읽어들임
for line in sys.stdin:
    line = line.strip()  # 공백 및 개행 문자 제거
    movie_id, rating = line.split()  # 탭(\t) 또는 공백 기준 분리 (movie_id, rating)

    try:
        rating = float(rating)  # 문자열을 실수(float)형으로 변환
    except:
        continue  # 변환 실패 시 해당 줄은 무시하고 다음 줄로 넘어감

    # 현재 영화와 이전 영화가 같다면 집계
    if currunt_movie_id == movie_id:
        currunt_count += 1             # 평점 개수 증가
        currunt_sum += rating          # 평점 합계 누적
    else:
        # 영화가 바뀌는 시점: 이전 영화에 대해 평균 계산 후 출력
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum / currunt_count  # 평균 계산
            print(f'{currunt_movie_id}\t{currunt_avg}')  # 영화 ID와 평균 평점 출력

        # 다음 영화의 데이터로 초기화
        currunt_movie_id = movie_id
        currunt_count = 1
        currunt_sum = rating

# 마지막 영화에 대한 평균도 출력 (루프 종료 후)
currunt_avg = currunt_sum / currunt_count
print(f'{currunt_movie_id}\t{currunt_avg}')