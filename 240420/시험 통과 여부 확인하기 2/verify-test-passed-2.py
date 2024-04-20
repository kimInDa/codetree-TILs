# 변수 선언, 입력
n = int(input())
cnt = 0;

# 결과 출력
for i in range(n):
    # 점수 입력
    scores_arr = list(map(int,input().split())) 

    # 점수 합계 구하기
    sum_val = 0;
    for elem in scores_arr:
        sum_val += elem

    # 평균에 따른 결과 출력
    avg_val = sum_val / len(scores_arr)
    if(avg_val >= 60):
        print("pass")
        cnt += 1
    else:
        print("fail")

# 통과한 학생 수 출력
print(cnt)