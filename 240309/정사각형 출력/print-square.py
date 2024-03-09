# 변수 선언, 입력
n = int(input())
cnt = 1

# 출력
for _ in range(n):
    for _ in range(n):
        print(cnt, end = " ")
        cnt += 1
    
    print()