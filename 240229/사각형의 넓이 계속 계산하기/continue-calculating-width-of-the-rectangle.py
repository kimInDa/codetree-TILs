# 사각형이 넓이를 문자 C가 나올 때까지 출력
while True:
    arr = input().split()
    w = int(arr[0])
    h = int(arr[1])
    c = arr[2]

    print(w * h)

    if c == "C":
        break