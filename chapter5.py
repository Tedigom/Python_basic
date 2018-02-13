# -*- coding: utf-8 -*-
print('한글이 이제 될까?')

#인사 로봇
number = 20
greeting = '안녕하세요!'
place = '세계'
welcome = '환영합니다'

#old way (기존방법)
print(number, '번 손님', greeting, '.', place, '에 오신것을', welcome, '!')
#이게 더 편할 때도 있겠지만

base = '{}번 손님, {}. {}에 오신것을 {}!'
new_way = base.format(number,greeting,place,welcome)
print(base)
print(new_way)


mine = '가위'
yours = '바위'
result = '졋다...'

print('나는 {}, 너는 {}, 그래서{}'.format(mine,yours,result))
