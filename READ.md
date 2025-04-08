# hadoop command

`ls`
- hdfs dfs -ls /
- hdfs dfs -ls <확인하고 싶은 경로>

- `mkdir`
    - `hdfs dfs -mkdir /input`
    - hdfs dfs -mkdir <생성하고싶은폴더이름>

- `put`
    - hdfs dfs -put <업로드 할 파일경로> <업로드 할 위치>
    
- `cat` //출력하고 싶은 데이터를 전체출력
    - hdfs dfs -cat <출력하고 싶은 파일경로>

- `head`, `talil`
    - hdfs dfs -head <출력하고 싶은 파일 경로>

- C:\Windows\System32\drivers\etc => hosts
- 맨 아래 127.0.0.1	<컴퓨터 이름>.

- `rm`
    - hdfs dfs -rm <지울파일경로>
    - 폴더를 삭제할 경우 -r 옵션 추가 //hdfs dfs -rm -r /input


    <!-- chmod +x mapper.py / 실행권한 주기
    chmod -x mapper.py / 실행권한 삭제 -->