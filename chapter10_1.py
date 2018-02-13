# -*- coding: utf-8 -*-

list = [1,2,3,5,7,2,5,237,55]

for val in list:
    if val % 3 == 0:
        print(val)
        break

""" break : 반복문을 종료 시키는 기능
    continue : 반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능"""

for i in range(10):
    if i%2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)
