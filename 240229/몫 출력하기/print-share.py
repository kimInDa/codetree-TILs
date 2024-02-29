# 변수 선언
cnt = 0

while True:
    if cnt >= 3:
        break
    else:
        n = int(input())
        if n % 2 == 0:
            print(n // 2)
            cnt += 1