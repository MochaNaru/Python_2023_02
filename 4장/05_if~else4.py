'''
    작성일 : 2023년 09월 20일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  선택문 if ~ else
            년도를 입력 받아 윤년인지 아닌지 판단하는 프로그램.
            
            윤년? 1년동안 날짜의 수가 366일이 되는 해
            연도가 4로 나누어 떨어지는 것
            연수가 4로 나우어 떨어져도, 100으로는 나누어 떨어지지 않아야 한다.
            연수가 400으로 나누어 떨어지는 해는 무조건 윤년으로 한다.
'''

#1. 연도를 입력 받는다.

year = int(input("연도를 입력하시오. : "))

#2. 판단.

if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print(year,"년은 윤년입니다.")
else :
    print(year,"년은 윤년이 아닙니다.")