# 변수 선언, 입력
n = int(input())
cnt = 'A'

# 아스키 코드를 이용한 알파벳 출력
for i in range(n):
    for _ in range(i + 1):
        print(cnt, end = "")
        cnt = chr(ord(cnt) + 1)
        if ord(cnt) > ord("Z"):
            cnt = "A"
    print()