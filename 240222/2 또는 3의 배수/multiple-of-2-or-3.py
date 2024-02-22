# 변수 선언, 입력
n = int(input())

# 출력
for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        print(1, end = ' ')
    else:
        print(0, end = ' ')