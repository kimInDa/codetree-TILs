# 변수 선언, 입력
inp = input().split()
a = int(inp[0])
b = int(inp[1])

#출력
if a <= b:
    print(b - a)
if a > b:
    print(a - b)