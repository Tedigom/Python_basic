# -*- coding: utf-8 -*-

""" dictionary """
import random

wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
    }


messeges = {
        'win' : '이겼다',
        'draw' : '비겼다',
        'lose' : '졌다.'
    }

computerCoice = ['가위','바위','보']

print(wintable['가위'])

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

inputV = input('뭐 낼건데?')

result = rsp(inputV,random.choice(computerCoice))


print(messeges[result])
