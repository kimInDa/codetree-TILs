# 변수 선언, 입력
n = int(input())

# 두 개의 직각삼각형 출력
for i in range(n, 0, -1):
    for _ in range(i):
        print("*", end ="")
    
    for _ in range((n * 2) - (i * 2)):
        print(" ", end = "")

    for _ in range(i):
        print("*", end ="")
    
    print()


# 3 -> 3 0 3
# 2 -> 2 2 2
# 1 -> 1 4 1

# 4 -> 4 0 4
# 3 -> 3 2 3
# 2 -> 2 4 2
# 1 -> 1 6 1