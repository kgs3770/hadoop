import sys  # 표준 입력(stdin)을 읽기 위해 sys 모듈을 임포트

# 표준 입력으로부터 한 줄씩 읽기
for line in sys.stdin:
    line = line.strip()  # 줄 끝의 개행 문자나 불필요한 공백 제거

    fields = line.split(',')  # 쉼표를 기준으로 문자열 분할 -> 리스트 형태로 반환
    # 예: ['1', '296', '5.0', '11133451414']
    # 일반적으로 사용자 ID, 영화 ID, 평점, 타임스탬프 순서

    movie_id = fields[1]  # 두 번째 항목: 영화 ID
    rating = fields[2]    # 세 번째 항목: 평점

    print(f'{movie_id}\t{rating}')  # 영화 ID와 평점을 탭으로 구분하여 출력