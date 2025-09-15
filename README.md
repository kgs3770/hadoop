# hadoop command

- `ls`
    - `hdfs dfs -ls /`
    - hdfs dfs -ls <확인하고싶은경로>

- `mkdir`
    - `hdfs dfs -mkdir /input`
    - hdfs dfs -mkdir <생성하고싶은폴더이름>

- `put`
    - hdfs dfs -put <업로드할 파일경로> <업로드할 위치>

- `cat`
    - hdfs dfs -cat <출력하고싶은 파일 경로>

- `head`, `tail`
    - hdfs dfs -head <출력하고싶은 파일 경로>

- `rm`
    - hdfs dfs -rm <지울파일경로>
    - 폴더를 삭제할 경우 -r 옵션 추가
