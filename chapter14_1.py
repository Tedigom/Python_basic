# -*- coding: utf-8 -*-
class Human( ):
    '''인간'''
    # __(언더바 2개) : 특별한 함수(특수 메소드)
    def __init__(self, name, weight):
        '''초기화 함수'''
        print("__init__ 실행")
        self.name = name
        self.weight = weight
        print("이름은 {}, 몸무게는 {}".format(name,weight))

    def __str__(self):
        '''문자열화 함수  --> 인스턴스가 문자열로 어떻게 표현되는지 결정해줌'''
        return "{}(몸무게 {}kg)".format(self.name, self.weight)

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

person = Human("사람",60.5)
print(person.name)
