# 변수 선언, 입력
arr = list(map(int, input().split()));
result_arr= []

# 0 이전까지 숫자 배열에 저장
for elem in arr:
    if elem == 0:
        break;
    else:
        result_arr.append(elem);

# 가장 나중에 입력된 정수부터 차례대로 출력
for i in range(len(result_arr) - 1, -1, -1):
    print(result_arr[i], end = " ")