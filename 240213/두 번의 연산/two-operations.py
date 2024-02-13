# 변수 선언, 입력
a = int(input())

# 출력
if a % 2 == 1:
    a += 3
if a % 3 == 0:
    a = a // 3
print(a)