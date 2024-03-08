# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# a행 b열 숫자 출력
for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i * j, end = " ")
    
    print()