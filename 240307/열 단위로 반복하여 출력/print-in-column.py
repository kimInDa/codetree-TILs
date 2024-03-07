# 변수 선언, 입력
n = int(input())

# 열 단위로 반복하여 출력
for i in range(1, n + 1):
    for j in range(n):
        print(i, end = "")
    
    print()