# 변수 선언, 입력
n = int(input())
cnt = n

# 출력
for i in range(n):
    for j in range(cnt, n + 1):
        print(j, end = " ")
        
    cnt -= 1

    print()