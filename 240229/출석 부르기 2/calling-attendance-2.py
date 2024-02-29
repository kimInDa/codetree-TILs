# while문을 활용하여 번호에 따른 이름 출력
while True:
    n = int(input())
    if n == 1:
        print("John")
    elif n == 2:
        print("Tom")
    elif n == 3:
        print("Paul")
    elif n == 4:
        print("Sam")
    else:
        print("Vacancy")
        break