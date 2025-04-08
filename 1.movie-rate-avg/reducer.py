import sys

# '296\t5.0'
currunt_movie_id = None
currunt_sum = 0
currunt_count = 0

for line in sys.stdin:
    line = line.strip()
    movie_id, rating = line.split()
    
    try:
        rating = float(rating)
    except:
        continue #// 문제가 발생하면 걍 넘어감

    if currunt_movie_id == movie_id:
        currunt_count += 1 
        currunt_sum += rating
    else: #영화가 바뀐시점
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum / currunt_count
            print(f'{currunt_movie_id}\t{currunt_avg}')
        
        #데이터 초기화
        currunt_movie_id
        currunt_count = 1
        currunt_sum = rating

currunt_avg = currunt_sum / currunt_count
print(f'{currunt_movie_id}\t{currunt_avg}')