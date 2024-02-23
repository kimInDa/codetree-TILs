# 변수 선언
cnt = 0

# 카운트
for i in range(5):
    n = int(input())
    if n % 2 == 0:
        cnt += 1

# 출력
print(cnt)