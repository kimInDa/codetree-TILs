# 변수 선언, 입력
arr = input().split()
sum_val = 0

# 10개 원소의 합 구하기
for i in range(10):
    sum_val += int(arr[i])

# 출력
print(sum_val)

# # 풀이 2. for in 이용
# # 입력 받은 수를 배열에 숫자로 변환하여 저장
# arr = list(map(int, input().split()))
# sum_val = 0

# # 입력 받은 수를 더하기
# for elem in arr:
#     sum_val += elem

# # 합 출력
# print(sum_val)