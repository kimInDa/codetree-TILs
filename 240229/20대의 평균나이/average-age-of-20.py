# 20대인 사람의 평균 구하기
sum_val = 0
cnt = 0

while True:
    # 변수 선언, 입력
    n = int(input())

    if n > 29 or n < 20:
        break
    else:
        sum_val += n
        cnt += 1

print(f"{sum_val / cnt:.2f}")