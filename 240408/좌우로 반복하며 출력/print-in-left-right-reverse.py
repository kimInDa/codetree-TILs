# 변수 선언, 입력
n = int(input())

# 행에 따라 정수 좌우 반복 출력
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(1, n + 1):
            print(j, end = "")
    else:
        for j in range(n, 0, -1):
            print(j, end = "")
    
    print()