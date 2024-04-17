# 정수 10개 입력 
arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

# 0 이전까지의 인덱스와 합 구하기
for elem in arr:
    if elem == 0:
        break
    else:
        cnt += 1
        sum_val += elem


# 0 이전까지의 합과 평균 출력
print(sum_val, f"{sum_val/cnt:.1f}")