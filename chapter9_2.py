# -*- coding: utf-8 -*-

list = [1,2,3,4,5]
for a in enumerate(list):
    print('{}번째 값: {}'.format(*a))
""" *a : 튜플을 쪼개라"""

ages = {'Tod':35, 'Jane':23, 'paul':62}
for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))
