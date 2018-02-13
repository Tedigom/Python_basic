# -*- coding: utf-8 -*-

"""list 에서의 for 문"""

seasons = ['봄','여름','가을','겨울']

for season in seasons:
    print(season)

"""dictionary에서의 for문"""
ages ={'Tod':35,'Jane':23,'Paul':62}

"""키만 출력"""
for key in ages.keys():
    print(key)

"""value만 출력"""d
for value in ages.values():
    print(value)

""" .keys()를 생략해도 괜찮음"""
for keys in ages:
    print('{}의 나이는 {}이다.'.format(keys,ages[keys]))


for key,value in ages.items():
    print('{}의 나이는 {}이다.'.format(key,value))
