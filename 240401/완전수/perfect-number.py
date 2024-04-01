# 변수 선언, 입력
arr = input().split()
start = int(arr[0])
end = int(arr[1])
cnt = 0;

# start와 end 사이의 수 중 완전수의 개수 출력
for i in range(start, end + 1):
    sum = 0;

    # i의 진약수의 합 구하기
    for j in range(1, i):
        if i % j == 0:
            sum += j
    
    # 완전수의 개수 구하기
    if sum == i:
        cnt += 1

print(cnt)