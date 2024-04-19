# 10개의 정수 입력받기
arr = list(map(int, input().split()))

# 변수 선언
cnt = 0;
sum_val = 0;

# 0 이전까지의 수 중 2의 배수 갯수와 합계 구하기
for elem in arr:
    if elem == 0:
        break;
    if elem % 2 == 0:
        cnt += 1
        sum_val += elem

# 출력
print(cnt, sum_val)