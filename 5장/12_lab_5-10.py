'''
    작성일 : 2023년 10월 04일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  사용자가 입력한 숫자들을 더하는 프로그램을 작성
            yes 일 동안만 반복
            교재 133 페이지
'''

total = 0 #숫자 변수를 초기화

choice = "yes" # 종료조건 변수저장

while choice == "yes" : #yes 가 아니면 종료
    num = int(input("숫자를 입력하세요. : ")) #숫자를 입력받음
    total += num #입력받은 숫자를 total에 저장
    choice = input("계속?(yes or no) : ") #반복할지 말지 여부를 물어봄
    
print("합계는 : ", total) #입력받은 숫자의 합계를 출력