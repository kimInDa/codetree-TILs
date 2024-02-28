# 입력값에 따라 출력
while True:
    # 변수 선언, 입력
    n = int(input())

    # 입력값이 25일 때
    if n == 25:
        print("Good")
        break
    # 입력값이 25보다 작을 때
    elif n < 25:
        print("Higher")

    # 입력값이 25보다 클 때
    else:
        print("Lower")