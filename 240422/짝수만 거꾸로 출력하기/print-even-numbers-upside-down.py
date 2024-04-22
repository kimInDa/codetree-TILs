# 정수의 갯수와 정수 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 짝수를 저장할 배열
even_arr = [];

# 입력된 수가 짝수이면 배열에 저장
for elem in arr:
    if(elem % 2 == 0):
        even_arr.append(elem)

# 배열 뒤집기
reversed_even_arr = even_arr[::-1]

# 짝수 배열 출력하기
for elem in reversed_even_arr:
    print(elem, end = " ")