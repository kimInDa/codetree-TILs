# 변수 선언, 입력
n = int(input())

# n길이의 직각삼각형 출력
for i in range(n):
    for _ in range(i + i + 1):
        print("*", end = "")
    
    print()