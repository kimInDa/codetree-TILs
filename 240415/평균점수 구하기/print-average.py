# 학생 8명의 점수 입력
arr = list(map(float, input().split()))
sum_val = 0;

# 학생 점수 총합 구하기
for elem in arr:
    sum_val += elem

# 학생 8명의 평균점수 출력
print(f"{sum_val/len(arr):.1f}")