# 변수 선언, 입력
a = int(input())

# 출력
if a % 2 == 0:
    a /= 2

if a % 2 != 0:
    a = (a + 1) / 2
print(int(a))