def function() :
    print('Hi function?!')

function()

def function2(number) :
    rounded = round(number)
    print(rounded)

function2(3.34)

def add_10(value) :
    return 10
    result = value + 10
    return result

n = add_10(42)
print(n)
