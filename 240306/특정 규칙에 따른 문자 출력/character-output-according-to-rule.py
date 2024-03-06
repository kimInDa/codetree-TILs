# 규칙에 따른 문자 출력

# 변수 선언, 입력
n = int(input())

# 상단부
for i in range(n):
    # 공백 출력
    for j in range(n - 1 - i):
        print(" ", end = " ")
    
    # @ 출력
    for j in range(i + 1):
        print("@", end = " ")
    
    print()

# 하단부
for i in range(n - 1):
    # @ 출력
    for j in range(n - 1 - i):
        print("@", end = " ")
        
    print()