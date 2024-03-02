# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

satisfied = True

# a이상 b이하에 c의 배수가 없는지 판별
for i in range(a, b + 1):
    if i % c != 0:
        satisfied = True

# c의 배수가 없다면 "YES", 있다면 "NO"를 출력
if satisfied == True:
    print("YES")
else:
    print("No")