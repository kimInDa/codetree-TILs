# 변수 선언, 입력
cnt_subject = int(input())
arr_grade = list(map(float, input().split()))

avg_grage = sum(arr_grade) / cnt_subject

# 출력
print(f"{avg_grage:.1f}")

if avg_grage >= 4.0:
    print("Perfect")
elif avg_grage >= 3.0:
    print("Good")
else:
    print("Poor")