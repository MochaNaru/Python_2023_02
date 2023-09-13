'''
    작성일 : 2023년 09월 13일
    작성자 : 학과 학번 이름
    설명 : 90페이지 문제 3.9
            평균 시속과 이동시간을 입력받아
            이동시간은 시,분,초 단위로 출력하고,
            이동한 거리를 계산하여 출력하시오.
'''

#시속과 시간을 입력
avg  = float(input("평균 시속을 입력하시오. : "))
total_hours = float(input("이동 시간을 입력하시오. : "))

#이동 거리를 구하는 식
move = avg * total_hours

#이동 시간을 구하는 식

hours = int(total_hours)  # 정수 부분은 시간
decimal_part = total_hours - hours  # 소수 부분

minutes = int(decimal_part * 60)  # 소수 부분을 분으로 변환 (1시간 = 60분)
seconds = int((decimal_part * 3600) % 60)  # 소수 부분을 초로 변환 (1분 = 60초)

print("평균 시속 : {:.2f} km/h" .format(avg))
print("이동 시간 : {} 시간 {} 분 {}초 ".format(hours, minutes, seconds))
print("이동 거리 : {:.3f} km" .format (move)) 