# -*- coding: utf-8 -*-

text = 100%

try:
     number = int(text)
 except ValueError:
     print('{}는 숫자가 아니다.'.format(text))


""" 예외처리
try:
    #에러가 발생할 가능성이 있는 코드
except Exception: #에러 종류
    #에러가 발생할 경우 처리할 경우( 경우에 따라 예외처리 대신 if else를 사용할 수 있다.)
"""


def safe_pop_print(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없다.'.format(index))


""" 예외의 이름을 모를 때에는 except 뒤에 아무것도 넣지 않아도 된다.
try:
    #에러가 발생할 가능성이 있는 코드
except:
    print("에러가 발생하였다.")

or

try:
    #에러가 발생할 가능성이 있는 코드
except Exception as ex:
    print("에러가 발생하였다.", ex)  # ex는 발생한 에러의 이름을 받아오는 변수

"""
