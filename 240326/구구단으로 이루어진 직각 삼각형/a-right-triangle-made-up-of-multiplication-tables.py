# 변수 선언, 입력
n = int(input())
cnt = n

# 직각삼각형 모양으로 구구단 출력
for i in range(1, n + 1):
    for j in range(1, cnt + 1):
        print(f"{i} * {j} = {i * j}", end = " ")
        if j != cnt:
            print("/", end = " ")
    cnt -= 1
    print()