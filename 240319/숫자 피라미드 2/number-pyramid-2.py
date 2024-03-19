# 변수 선언, 입력
n = int(input())
cnt = 1

# i번째 줄에 i개의 숫자 출력
for i in range(1, n + 1):
    for j in range(i):
        print(cnt, end = " ")
        cnt += 1
    print()