# 변수 선언, 입력
sum_val = 0
cnt = 0

for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        sum_val += n
        cnt += 1

avg = sum_val /cnt

# 출력
print(sum_val, f"{avg:.1f}")