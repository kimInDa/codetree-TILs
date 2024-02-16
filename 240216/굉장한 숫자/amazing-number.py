# 변수 선언, 입력
n = int(input())

# 출력
if (n % 2 == 1 and n % 3 == 0) or (n % 2 == 0 and n % 5 == 0):
    print("true")
else:
    print("false")