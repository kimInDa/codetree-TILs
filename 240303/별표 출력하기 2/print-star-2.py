# 변수 선언, 입력
n = int(input())

# 직각삼각형 출력
for i in range(n, 0, -1):
    for _ in range(i):
        print("*", end = ' ')
    print()

# 해설
# for i in range(n):
#     for _ in range(n - i):
#         print("*", end = ' ')
#     print()