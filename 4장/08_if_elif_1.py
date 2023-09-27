'''
    작성일 : 2023년 09월 27일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  점수를 입력받아 학점을 출력하시오.
            90 ~ 100 A : 학점
            80 ~ 89 B : 학점
            70 ~ 79 C : 학점
            60 ~ 69 D : 학점
            0 ~ 59 F : 학점
            
    알고리즘 : 1. 점수를 입력받는다.
                2. 점수를 판단하여 학점을 출력한다.
'''

#점수를 입력받는다.
score = int(input("점수 입력 : "))

# 판단.
# 이 코드는 논리 오류가 발생한다.
print("::: 첫 번째 성적 처리 :::")
if score >= 90 :
    print("A 학점 입니다.")
elif score >= 80 :
    print("B 학점 입니다.")
elif score >= 70 :
    print("C 학점 입니다.")
elif score >= 60 :
    print("D 학점 입니다.")
else :
    print("F 학점 입니다.")

print() #빈줄 출력

#정확한 범위를 지정하자. - 성적의 범위를 벗어나면 잘못된 점수 입력입니다. 출력
print("::: 두 번째 성적 처리 :::")

if (90 <= score <= 100) :
    print("A 학점 입니다.")
elif (80 <= score and score <= 89) :
    print("B 학점 입니다.")
elif (70 <= score and score <= 79) :
    print("C 학점 입니다.")
elif (60 <= score and score <= 69) :
    print("D 학점 입니다.")
elif (0 <= score and score <= 59) :
    print("F 학점 입니다.")
else :
    print("잘못된 점수 입력입니다.")
    
print()

# 점수는 무조건 0~100점 사이입니다. - 아니면 잘못된 입력입니다.
print("::: 세 번째 성적 처리 :::")

if 0 <= score <= 100 :
    if score >= 90 :
        print("A 학점 입니다.")
    elif score >= 80 :
        print("B 학점 입니다.")
    elif score >= 70 :
        print("C 학점 입니다.")
    elif score >= 60 :
        print("D 학점 입니다.")
    else : # A ~ D 학점이 아니면 출력
        print("F 학점 입니다.")
else : # 0~100점이 아니면 출력
    print("점수를 잘못 입력하셨습니다.")