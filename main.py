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