# 만들어놓은 usecsv 묘듈을 사용해 보자

import usecsv   # sys.path 를 이용해 모듈 저장가능한 경로를 파악하고 그 디렉토리에 모듈을 넣는다.

# csv파일을 파이썬에서 사용할 수 있는 리스트 형태의 (csv 형태) 자료로 변환하여 b_file 변수에 저장 
b_file = usecsv.opencsv('b.csv')

usecsv.writecsv('과일.csv', b_file)




