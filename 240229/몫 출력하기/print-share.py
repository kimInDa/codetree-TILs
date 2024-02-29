# 변수 선언
cnt = 0

# 짝수를 2로 나눈 몫을 3번까지 출력
while True:
    if cnt >= 3:
        break
    else:
        n = int(input())
        if n % 2 == 0:
            print(n // 2)
            cnt += 1