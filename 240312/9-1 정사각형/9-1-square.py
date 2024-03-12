# 변수 선언, 입력
n = int(input())
cnt = 9

# 9부터 1까지 1씩 감소하는 숫자로 이루어진 n * n 정사각형 출력
for i in range(n):
    for j in range(n):
        print(cnt, end = "")
        cnt -= 1
        if cnt == 0:
            cnt = 9
    print()  # 각 행이 끝날 때마다 줄바꿈을 해줍니다.