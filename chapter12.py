# -*- coding: utf-8 -*-

a = 10
if a<0 and 2**a>1000 and a%5 ==2 and round(a) ==a:
    print("복잡한 식")

def return_false():
    print("함수 return false")
    return False

def return_true():
    print("함수 return true")
    return True

print("테스트 1")
a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)


print("테스트 2")
if return_false() and return_true():
    print("True")
else:
    print(False)



dic = {"key2":"Value1"}
if "Key1" in dic and dic["key1"] == "Value1":
    print("key1도 있고, 그값은 Value1")
else:
    print("아니다.")


"""
true False

숫자 0을 제외한 모든 수 - true
빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
아무 값도 없다는 의미인 None - false
빈문자열을 제외한 모든 문자열 - true
"""

value = input('입력') or '아무것도 못받았어'
print('입력받은 값>',value)
