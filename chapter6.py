# -*- coding: utf-8 -*-
# list == array

list = ['가위','바위','보']
list2 = [37,23,10,33,29,40]

print(list)
print(list2)


list[0] = '바위'
print(list[0])
print(list)


#list[-1]은 뒤에서 첫번째라는 뜻
print(list[-1])


#추가
list2.append(16)
print(list2)

list3 = list2 + [16]
print(list3)

list4 = list2 + list3

#13번째의 원소를 지운다
del list4[12]
#특정값 지우기 ( 여러개가 있을때 가장먼저 나오는 값 하나만 지운다. )
list4.remove(40)

# 원소가 들어있는지 없는지의 여부
numbers = [1,2,3,4,5]
if 5 in numbers :
    print('5가 있다.')
