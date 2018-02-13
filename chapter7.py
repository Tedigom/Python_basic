# -*- coding: utf-8 -*-

#for - in

patterns = ['가위','보','보','가위','가위''바위','가위','보']

for pattern in patterns:
    print(pattern)


# for in range
# 0,1,2,3,4를 순서대로 출력하기

for i in range(10):
    print(i)


# range(n) : [0,1,2,...n-1]

#응용
names = ['철수','영희','바둑이','귀도']

for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i+1, name))

print(' ')

for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))

    # for in list : 순회할 리스트가 정해져있을때
    # for in range() 순회할 횟수가 정해져 있을때
