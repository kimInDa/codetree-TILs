# 변수 선언
cnt = 0

# 카운트
for i in range(10):
    n = int(input())
    if n % 2 == 1:
        cnt += 1

# 출력
print(cnt)