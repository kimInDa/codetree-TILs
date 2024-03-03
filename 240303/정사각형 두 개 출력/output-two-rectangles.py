# 변수 선언, 입력
n = int(input())

# n * n 정사각형 2개 출력
for _ in range(2):
    
    for _ in range(n):
        
        for _ in range(n):
            print("*", end = '')
        
        print()

    print()