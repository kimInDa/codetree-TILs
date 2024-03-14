# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# a와 b사이의 수 중 짝수의 구구단 출력
for i in range(1, 10):
    for j in range(b, a - 1, -1):
        if j % 2 == 0:
            print(f"{j} * {i} = { j * i }", end = "")
            if j > a:
                print(" / ", end = "")
    
    print()