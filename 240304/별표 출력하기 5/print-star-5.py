# 변수 선언, 입력
n = int(input())

# n길이의 직각삼각형 출력
for i in range(n, 0, -1):
    
    for _ in range(i):
        
        for _ in range(i):
            print("*", end = "")
        
        print(end = " ")

    print()