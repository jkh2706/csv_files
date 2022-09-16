# 인구중에서 외국인이 3% 가 넘는 구를 찾아보자

import usecsv

# 기존의 cites.csv파일을 csv 형태의 파일로 가공한다.
total = usecsv.opencsv('popSeoul.csv')  # csv형태의 리스트 객체를 만들어 total 변수에 저장한다.

# ','로 구분된 str 형태의 데이터를 usecsv 모듈의 switch메서드를 사용하여 int형 데이터로 재 가공한다
new_pop = usecsv.switch(total)

# 외국인 비율을 계산하도록 새로운 리스트를 만든다.
pop_for = new_pop[1] # 새로운 리스트의 첫 행을 지정한다.

# 외국인 비율이 3%를 초과하는 구만 포함하는 새로운 리스트를 만든다.
foreign_list = [['구', '외국인비율']]

for i in new_pop:
    foreign = 0
    try:                                    # 첫번째 원소의 str 타입의 자료로 인한 계산불가 에러를 무시하기 위해 try/except 구문사용
        foreign = round(i[2]/(i[1] + i[2]) * 100, 1)  # 전체인구대비 외국인 비율 계산(백분율)
        if foreign > 3:
            foreign_list.append([i[0],foreign])
    except:
        pass

# csv형태의 결과 파일을 csv파일로 저장하기
usecsv.writecsv('외국인비율_1.csv', foreign_list)