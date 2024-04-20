# 학생 수 입력 받기
n = int(input())

# 통과한 학생 수를 나타내는 변수
cnt = 0;

# 학생별 통과 여부 출력
for i in range(n):
    # 점수 입력
    scores_arr = list(map(int,input().split())) 

    # 점수 합계 구하기
    sum_val = 0;
    for elem in scores_arr:
        sum_val += elem

    # 평균 구하기
    avg_val = sum_val / len(scores_arr)
    
    # 평균에 따른 결과 출력
    if(avg_val >= 60):
        print("pass")
        cnt += 1
    else:
        print("fail")

# 통과한 학생 수 출력
print(cnt)