# csv 파일안의 문자를 숫자로 변환하는 코드를 만들어 usecsv모듈에 추가한다.

import usecsv, re 

# total = usecsv.opencsv('popSeoul.csv')  # usecsv 모듈의 opencsv 메서드로 'popSeoul.csv'파일을 열어 total 변수에 저장

# a = total[1]
a = ['Jongrogu',"151,767","11,093","27,394"]
for i in a:
    
    try:
        a[a.index(i)] = int(re.sub(',','',i))  # i.index[j]는 j의 인덱스, ','를 찾아 리스트를 정수로 변경
            
    except:  # 정수로 변경할 수 없는 문자열 혹은 특수문자가 오면 그냥 pass
        pass


print(a)
print(type(a[1]))