'''
    작성일 : 2023년 10월 04일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  조건에 따라 반복하는 while문
            교재 127 페이지
'''

#반복문에는 반드시 종료 조건이 있어야한다
#while True : 무한반복

under_construction = True #공사중

#True 일 동안 계속 반복(무한반복)
while under_construction :
    response = input("공사가 완료 되었씁니다?")
    if response == "예" :
        under_construction = False
        
print("루프를 탈출했습니다.")