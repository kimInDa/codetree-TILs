# 변수 선언, 입력
n = int(input())

# 상단 부분 그리기
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

# 하단 부분 그리기
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)