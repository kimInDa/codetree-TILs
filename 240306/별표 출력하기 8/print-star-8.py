# 변수 선언, 입력
n = int(input())

# 홀수줄은 1개, 짝수줄은 줄번호만큼 * 출력
for i in range(1, n + 1):
    if i % 2 == 0:
        for j in range(i):
            print("*", end = " ")
        print()
    else:
        print("*")