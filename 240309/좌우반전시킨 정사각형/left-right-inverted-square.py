# 변수 선언, 입력
n = int(input())

# 출력
for i in range(n,(n * n) + 1, +n):
    for j in range(i, (i // n) - 1, -(i // n)):
        print(j, end = " ")
        
    print()