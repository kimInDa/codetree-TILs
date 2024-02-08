# 변수 선언, 입력
arr = input().split()
width = int(arr[0])
height = int(arr[1])

# 길이 변형
width += 8
height *= 3

# 출력
print(f"{width}\n{height}\n{width * height}")