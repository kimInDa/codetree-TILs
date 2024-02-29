# 변수 선언
sum_val = 0
cnt = 0

while True:
    # 변수 선언, 입력
    n = int(input())

    # 나이가 20대가 아닌 경우 loop 종료
    if n > 29 or n < 20:
        break

    # 나이가 20대인 경우 나이의 총합과 인원수 구하기
    else:
        sum_val += n
        cnt += 1

# 20대인 사람의 평균 출력
print(f"{sum_val / cnt:.2f}")