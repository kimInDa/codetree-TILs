# 변수 선언, 입력
inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
arr = [a, b, c]

# 출력
print(sum(arr))
print(sum(arr) // len(arr))