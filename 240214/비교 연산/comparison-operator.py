# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# 출력
result1 = 1 if a >= b else 0
print(result1)

result2 = 1 if a > b else 0
print(result2)

result3 = 1 if b >= a else 0
print(result3)

result4 = 1 if b > a else 0
print(result4)

result5 = 1 if a == b else 0
print(result5)

result6 = 1 if a != b else 0
print(result6)