# 함수 open_csv 와 write_csv 를 이용하여 csv 파일을 다루는 모듈을 만들어 보자

import csv 

def opencsv(file):
    with open(file, 'r', encoding='utf-8-sig') as f:  # csv 파일 맨처음에 나타나는 \ufeff를 없애주기위해서 인코딩을 utf-8-sig
        csv_file = csv.reader(f)

        a_list = []
        for i in csv_file:
            a_list.append(i)

    return a_list

def writecsv(file, data_list):
    with open(file, 'w', newline='', encoding='utf-8') as f:  # 새 csv 파일을 쓰기모드로 연다.
        csv_obj = csv.writer(f, delimiter=',')  # csv쓰기 객체를 만든다. ','로 구분되는 리스트를 새 파일에 쓴다.
        # csv 형태의 리스트를 파일에 쓸때는 writerow()를 사용한다.
        csv_obj.writerows(data_list)


