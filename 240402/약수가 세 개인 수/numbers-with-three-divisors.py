# 변수 선언, 입력
arr = input().split()
start = int(arr[0])
end = int(arr[1])
cnt = 0

# start와 end 사이에 약수개 3개인 수의 갯수 구하기
for i in range(start, end + 1):
    num = 0
    for j in range(1, i + 1):
        if i % j == 0:
            num += 1
    if num == 3:
        cnt += 1

print(cnt)