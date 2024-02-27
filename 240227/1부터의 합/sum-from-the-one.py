# 변수 선언, 입력
n = int(input())
sum_val = 0

# 1부터 n까지 차례대로 더한 값이 n이상이 되는 순간 합한 값을 출력
for i in range(1, n + 1):
    sum_val =+ i
    if sum_val >= n:
        break

print(sum_val)