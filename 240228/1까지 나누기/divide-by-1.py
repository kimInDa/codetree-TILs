# 변수 선언, 입력
n = int(input())
cnt = 0

# n을 1부터 1씩 증가한 수로 나누었을 때 1이하가 되는 순간까지 나눈 횟수 출력
for i in range(1, n + 1):
    n = n // i
    cnt += 1
    if n <= 1:
        break

print(cnt)