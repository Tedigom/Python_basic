# -*- coding: utf-8 -*-

"""
자료형
type( a ) #type(변수명) : 자료형
ex)
s = "Hello world"
type(s) ==> class, str형

isinstance( 42, int) #isinstance(값, 자료형) -> 자료형 검사
"""

"""
클래스 : 함수나 변수들을 모아놓은 집합체
인스턴스 : 클래스에 의해 생성된 객체, 인스턴스 각자 자신의 값을 가지고 있다.

class 클래스명():

클래스와 인스턴스를 이용하면 데이터와 코드를
사람이 이해하기 쉽게 포장할 수 있다.

클래스에 함수를 넣을 수 있다.

"""

#make class

class Human():
    '''사람 에 대한 클래스'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

print(person1.language)
print(person2.language)

person1.name = '서울 시민'
person2.name = '인도인'

def speak(person):
    print("{}이 {}로 말을 한다.".format(person.name, person.language))

Human.speak = speak

person1.speak()
person2.speak()
