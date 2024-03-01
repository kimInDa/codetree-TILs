# 변수 선언, 입력
n = int(input())
x = 0

while n != 1:
    n //= 2
    x += 1

print(x)