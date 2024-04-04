# 변수 선언, 입력
n = int(input())

# n번에 걸쳐 주어지는 a, b 
# a와 b 사이의 수 중 짝수의 합 출력
for _ in range(n):
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    sum = 0
    for j in range(a, b + 1):
        if j % 2 == 0:
            sum += j

    print(sum)