# 변수 선언, 입력
n = int(input())
sum_val = 0

# 1부터 n-1까지의 수중에서 약수의 합 구하기
for i in range(1, n):
    if n % i == 0:
        sum_val += i

# 출력
if sum_val == n:
    print("P")
else:
    print("N")