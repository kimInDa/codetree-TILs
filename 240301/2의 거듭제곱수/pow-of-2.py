# 변수 선언, 입력
n = int(input())
x = 0

# n이 2의 몇제곱인지(x) 구하기
while n != 1:
    n //= 2
    x += 1

# 출력
print(x)