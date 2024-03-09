# 변수 선언, 입력
n = int(input())
cnt = 1

# 출력
for i in range(n):
    for j in range(n):
        print(cnt, end = " ")
        cnt += 1
    
    print()