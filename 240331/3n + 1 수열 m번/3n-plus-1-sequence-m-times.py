# 변수 선언, 입력
m = int(input())

for _ in range(m):
    n = int(input())
    cnt = 0;

    while n != 1:
        if(n % 2 == 0):
            n /= 2
        else:
            n = (n * 3) + 1
        cnt += 1
    
    print(cnt)