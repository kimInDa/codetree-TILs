# 변수 선언, 입력
arr = input().split()

# 배열 요소 거꾸로 출력
reversed_arr = arr[::-1]

for elem in reversed_arr:
    print(elem, end = "")