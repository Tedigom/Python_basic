# -*- coding: utf-8 -*-

areas = []
for i in range(1,11):
    if i%2 ==0:
        areas = areas + [i*i]
print(areas)


#list comprehension
areas2 = [i*i for i in range(1,11) if i%2==0 ]
print("areas2",areas2)


'''List Comprehension
파이썬의 유용한 도구
예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
'''

'''Dictionary Comprehension
파이썬의 유용한 도구
예1 { "{}번".format(number):name for number, name in enumerate(students) } # [ 형식 for문 ]
예2

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {x:y for x,y in zip(product_list, price_list)}


'''
