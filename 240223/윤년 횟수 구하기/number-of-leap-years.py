# 변수 선언, 입력
n = int(input())
cnt = 0

# 카운트
for i in range(1, n + 1):
    if i % 4 == 0:
        if i % 100 != 0 or i % 400 == 0:
            cnt += 1

# 출력
print(cnt)