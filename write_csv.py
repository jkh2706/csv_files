# csv형태의 자료를 파이썬을 이용하여 엑셀에 써보자.
# csv.writer() 사용
# 미리 csv형태로 가공해놓은 write.csv파일을 도시.csv파일을 만들어 써본다.

import csv

data_list = [['양천구','강남구','강서구','송파구'],[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def write_csv(file, data_list):
    with open(file, 'w', newline='', encoding='utf-8') as f:  # 입력받은 파일을 쓰기모드로 연다.
        csv_obj = csv.writer(f, delimiter=',')  # csv쓰기 객체를 만든다. ','로 구분한다.

       
        # csv 형태의 리스트를 파일에 쓸때는 writerow()를 사용한다.
        csv_obj.writerows(data_list)


write_csv('cities.csv', data_list)


