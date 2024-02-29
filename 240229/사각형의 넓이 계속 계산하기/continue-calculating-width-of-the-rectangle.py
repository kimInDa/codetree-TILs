# 사각형의 넓이를 문자 C가 나올 때까지 출력
while True:
    # 변수 선언, 입력
    arr = input().split()
    w = int(arr[0])
    h = int(arr[1])
    c = arr[2]

    # 사각형의 넓이 출력
    print(w * h)

    # 문자 C가 나오면 loop 종료
    if c == "C":
        break