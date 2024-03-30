# 변수 선언, 입력
n = int(input())

for _ in range(n):
    arr = input().split(' ')
    a, b = int(arr[0]), int(arr[1])
    
    multiple_val = 1
    for j in range(a, b + 1):
        multiple_val *= j
    print(multiple_val)