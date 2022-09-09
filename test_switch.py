# usecsv 모듈의 switch 메서드 테스트

import usecsv  # usecv 모듈을 임포트한다.

listName = usecsv.opencsv('popSeoul.csv')  # csv파일을 열어 파이썬에서 사용할 수 있는 형태의 리스트 자료로 만든다.

new_list = usecsv.switch(listName)  # 만든 리스트파일에서 switch 메서드를 사용하여 str 자료를 ','를 없애고 실수형태로 만든다

print(new_list)

new_file = usecsv.writecsv('인구통계.csv', new_list)  # 실수형태의 자료를 다시 csv 파일로 만든다.
