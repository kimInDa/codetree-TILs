# 변수 선언, 입력
n = int(input())

# 별표 출력
for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()