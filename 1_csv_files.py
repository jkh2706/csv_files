# csv 모듈을 이용하여 csv파일을 읽어보자

import csv

with open('a.csv', 'r', encoding='utf-8') as f:  
    csv_file = csv.reader(f)  # csv 파일을 읽으려면 csv 모듈의 reader()메서드를 사용한다.

# for i in csv_file:
#     print(i)

# 파이썬에서 csv 파일을 사용하기위해 csv파일을 리스트 형태로 바꾼다.
# with 문을 사용하면 파일이 열려있는 상태이므로 with문 안에 들여쓰기를 해서 for문을 돌려야 한다.
    new_list = []
    for i in csv_file:
        new_list.append(i)

print(new_list)

