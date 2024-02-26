# 변수 선언, 입력
n = int(input())
cnt = 0

# 1 ~ n 사이의 수 중에서 친근하지 않은 수의 개수 구하기
for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    
    cnt += 1

# 출력
print(cnt)