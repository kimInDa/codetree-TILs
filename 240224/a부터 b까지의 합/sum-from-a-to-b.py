# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0

for i in range(a, b + 1):
    sum_val += i

# 출력
print(sum_val)