# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

satisfied = False

# a와 b사에 c의 배수가 있는지 판단
for i in range(a, b + 1):
    if i % c == 0:
        satisfied = True

# c의 배수 여부에 따라 "YES" or "NO" 출력
if satisfied == True:
    print("YES")
else:
    print("NO")