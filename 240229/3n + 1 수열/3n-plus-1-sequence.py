# 변수 선언, 입력
n = int(input())
cnt = 0

# n이 1일 될 때까지 계산 횟수 구하기
while True:
    # n이 1이 되면 loop 종료
    if n == 1:
        break

    # n이 짝수면 2로 나누고 계산 횟수 증가
    elif n % 2 == 0:
        n = n // 2
        cnt += 1
    
    # n이 홀수면 3을 곱하고 1을 더한 후 계산 횟수 증가
    else:
        n = n * 3 + 1
        cnt += 1

# 계산 횟수 출력
print(cnt)