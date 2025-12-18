#Global키워드

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)



def op(a,b):
    add = a+b
    subtract = a-b
    multiply = a*b
    divide = a/b
    return add , subtract, multiply, divide

a,b,c,d = op(7,3)
print(a,b,c,d)