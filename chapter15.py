# -*- coding: utf-8 -*-

#inheritance(상속)
#자식 클래스가 부모 클래스의 내용을 가져다 슴

class Animal():

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("인사한다.")

class Cow(Animal):
    '''소'''


class Human(Animal):

    def wave(self):
        print("손을 흔든다.")

    def greet(self):
        self.wave()



class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다.")

    def greet(self):
        self.wag()



person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()
