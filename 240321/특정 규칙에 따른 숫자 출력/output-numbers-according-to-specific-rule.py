# 변수 선언, 입력
n = int(input())
cnt = 1

# 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(" ", end = " ")

    # 숫자 출력
    for j in range(n - i):
        print(cnt, end = " ")
        cnt += 1
        
        # 숫자는 9까지만 출력
        if cnt == 10:
            cnt = 1

    # 줄바꿈
    print()