# 학생 8명의 점수 입력
arr = list(map(float, input().split()))
sum_val = 0;

for elem in arr:
    sum_val += elem

print(f"{sum_val/len(arr):.1f}")