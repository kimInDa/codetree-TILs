# 변수 선언, 입력
arr = input().split()
sum_val = 0

# 10개 원소의 합 구하기
for i in range(10):
    sum_val += int(arr[i])

# 출력
print(sum_val)