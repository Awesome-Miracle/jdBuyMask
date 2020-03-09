# print('hello')

a = 1
b = [2, 3]

def func():
    global a
    a = 2
    print("in func a:", a)


if __name__ == '__main__':
    print("before func a:", a)
    func()
    print("after func a:", a)
