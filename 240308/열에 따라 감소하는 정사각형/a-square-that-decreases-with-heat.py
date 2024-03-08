# 변수 선언, 입력
n = int(input())

# n부터 1까지 숫자를 n번 출력하기
for i in range(n):
    for j in range(n, 0, -1):
        print(j, end = " ")
    
    print()