def input_function():
    while True:
        try:
            x = int(input("Введите валидное число:\n"))
            return x
        except:
            pass

def x3_1(x):
    return x * 3 + 1

def x2(x):
    return x // 2

def collatz():
    x = input_function()
    if x%2==0:
        print('x - чётное\nx/2 =', x2(x))
    else:
        print('x - нечётное\nx*3+1 =', x3_1(x))

collatz()