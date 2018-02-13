# -*- coding: utf-8 -*-

#raise

def rap(mine,yours):
    allowed = ['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
    #가위바위보 승패를 판단하는 코드

try:
    rsp('가위','바')
except ValueError:
    print('잘못된 값을 넣은것 같습니다.')

""" 예외 발생
사용자가 직접 에러를 발생시키는 기능
raise Exception # 에러 종류
많이 사용하면 코드를 읽기 어려워진다.
"""

school = {'1반': [172,186,193,177,160], '2반': [150,192,191]}
for class_number, students in school.items():
    for students in students:
        if student>190:
            print(class_number)
            raise StopIteration #예외가 발생하는 즉시 loop가 종료된다.

Except StopIteration:
    print('정상종료')
