# 변수 선언, 입력
n = int(input())

# 행 단위로 반복하여 숫자 출력
for i in range(n):
    for j in range(1, n + 1):
        print(j, end = "")
    
    print()