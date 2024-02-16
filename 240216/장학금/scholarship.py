# 변수 선언, 입력
arr = input().split()
mid = int(arr[0])
end = int(arr[1])

# 출력
if mid <= 90:
    print(0)   
elif end >= 95:
    print(100000)
elif end >= 90:
    print(50000)
else:
    print(0)