def input_function():
    while True:
        try:
            x = int(input("Введите валидное число:\n"))
            if x>=0:
                return x
            else:
                pass
        except:
            pass

def x3_1(x):
    return x * 3 + 1

def x2(x):
    return x // 2

def collatz(x):
    result = []
    while x>1:
        if x%2==0:
            x = x2(x)
        else:
            x = x3_1(x)
        result.append(x)
    return result
    
print('Результат:', collatz(input_function()))