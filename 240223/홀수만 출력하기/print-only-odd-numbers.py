# 변수 선언, 입력
n = int(input())

# 출력
for _ in range(n):
    num = int(input())
    if num % 2 == 1 and num % 3 == 0:
        print(num)