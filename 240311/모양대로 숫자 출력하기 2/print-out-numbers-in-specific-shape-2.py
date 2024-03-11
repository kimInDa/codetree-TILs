# 변수 선언, 입력
n = int(input())
cnt = 2

# n * n 크기의 정사각형 출력
for i in range(n):
    for j in range(n):
        print(cnt, end = " ")
        cnt += 2
        if cnt > 8:
            cnt = 2
            
    print()