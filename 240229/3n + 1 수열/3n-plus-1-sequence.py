# 변수 선언, 입력
n = int(input())
cnt = 0

# n이 1일 될 때까지 계산 횟수 구하기
while True:
    # n이 1이 되면 loop 종료
    if n == 1:
        break

    # n이 짝수면 2로 나누기
    elif n % 2 == 0:
        n = n // 2
    
    # n이 홀수면 3을 곱하고 1을 더하기
    else:
        n = n * 3 + 1

    # 계산 횟수 카운트    
    cnt += 1

# 계산 횟수 출력
print(cnt)