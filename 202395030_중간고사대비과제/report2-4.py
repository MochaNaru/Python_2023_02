'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 169 6.5 섭씨온도를 0도에서 50도까지 10도 단위로 증가시키면서
            이에 해당하는 화씨온도를 출력하는 프로그램을 작성.
            이를 위하여 섭씨온도를 인자로 받아서 화씨온도를 반환하는 cel2fah() 함수를 만들어라
'''

# 섭씨를 화씨로 변환하는 함수 정의
def cel2fah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 0도에서 50도까지 10도 단위로 섭씨 온도 변환하고 화씨 온도 출력
for celsius in range(0, 51, 10):
    fahrenheit = cel2fah(celsius)
    print(f"{celsius}도 섭씨는 {fahrenheit}도 화씨입니다.")