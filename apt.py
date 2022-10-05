# 실거래가 20억 이하 60m^2 초과 85m^2이하 매물을 추려내 보자
import usecsv 
import re 
# csv파일을 열어서 csv 형태의 리스트를 만들고 ","와 "."를 없애고 int 자료형을 포함하는 리스트를 만든다.
apt = usecsv.switch(usecsv.opencsv('kangnam_2022_09.csv'))

""" 
아래의 for 문의 내용은 usecsv 모듈의 switch 메소드에 추가한다.
# for i in apt:
   
#     for j in i:
#         try:
#             i[i.index(j)] = int(re.sub(r'[.]','',j))  # i.index(j)는 j의 인덱스, ','를 찾아 리스트를 정수로 변경하고 '.'를 없앤 정수형으로 만든다.
        
#         except:  # 정수로 변경할 수 없는 문자열 혹은 특수문자가 오면 그냥 pass
#             pass
"""       
result =[]

for i in apt:
   try:
        if i[8] <= 200000 and i[5] >6000 and i[5] <= 8500:
            result.append(i[:9])
   except:
        pass 

usecsv.writecsv('result.csv', result)
    
        