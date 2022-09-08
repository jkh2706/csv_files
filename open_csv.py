# csv파일을 파이썬에서 사용할 수 있는 csv형태로 만드는 함수를 작성해보자.
import csv

def opencsv(file):
    with open(file, 'r', encoding='utf-8-sig') as f:  # csv 파일 맨처음에 나타나는 \ufeff를 없애주기위해서 인코딩을 utf-8-sig
        csv_file = csv.reader(f)

        a_list = []
        for i in csv_file:
            a_list.append(i)

    return a_list 

result = opencsv('시험성적.csv')
print(result)

