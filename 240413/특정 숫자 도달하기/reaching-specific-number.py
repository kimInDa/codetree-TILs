# 변수 선언, 입력
arr = list(map(int, input().split()))
result_arr = [];
sum_val = 0;
avg_val = 0;

# 250 미만의 수로 이루어진 리스트 구하기
for elem in arr:
    if elem >= 250:
        break;
    else:
        result_arr.append(elem)

# 합계 구하기
for elem in result_arr:
    sum_val += elem

# 평균 구하기
avg_val = sum_val / len(result_arr)

# 합계와 평균 출력
print(sum_val, avg_val)