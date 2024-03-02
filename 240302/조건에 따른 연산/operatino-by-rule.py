# 변수 선언, 입력
n = int(input())
cnt = 0

# n이 처음으로 1000이상이 될 때까지 연산
while n < 1000:
    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = n * 2 + 2

    # 연산 횟수 세기
    cnt += 1

# 연산 횟수 출력
print(cnt)