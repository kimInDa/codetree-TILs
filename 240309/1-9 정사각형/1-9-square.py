# 변수 선언, 입력
n = int(input())
cnt = 1

# cnt를 사용하여 1씩 증가하는 n*n 정사각형 출력
for _ in range(n):
    for _ in range(n):
        print(cnt, end = "")
        cnt += 1
        if cnt == 10:
            cnt = 1
    print()