'''
    작성일 : 2023년 09월 13일
    작성자 : 학과 학번 이름
    설명 : 직각 삼각형의 빗변의 길이를 구하시오
'''

bottom = float(input("직삼각형 밑변의 길이를 입력하시오. : "))
height = float(input("직삼각형의 높이를 입력하시오. : "))

triangle = (bottom ** 2 + height ** 2) ** 0.5

print("밑변이 {} 이고 높이가 {} 일때 빗변은 {:.2f} 입니다".format(bottom, height, triangle))
