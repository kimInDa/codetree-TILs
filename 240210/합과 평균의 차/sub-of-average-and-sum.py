# 변수 선언, 입력
inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
arr = [a, b, c]

print(sum(arr))
print(sum(arr) // len(arr))
print(sum(arr) - sum(arr) // len(arr))