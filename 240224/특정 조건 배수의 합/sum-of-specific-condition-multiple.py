# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0

# a와 b 사이의 수 중 5의 배수의 합 구하기
# Case 1. b가 더 큰 경우
if a <= b:
    for i in range(a, b + 1):
        if i % 5 == 0:
            sum_val += i

# Case 2. a가 더 큰 경우
else:
    for i in range(b, a + 1):
        if i % 5 == 0:
            sum_val += i

# 출력
print(sum_val)