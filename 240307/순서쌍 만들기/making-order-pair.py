# 변수 선언, 입력
n = int(input())

# (n, n)부터 (1, 1)까지 순서쌍 출력
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(f"({i},{j})", end = " ")
    
    print()