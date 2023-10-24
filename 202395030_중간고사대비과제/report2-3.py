'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 169 6.1 n이라는 매개변수를 입력받아서 이 값의 제곱 값을 반환하는 square(n) 함수를 정의하고
            이 함수를 호출하여 3과 4의 제곱을 출력하는 프로그램
'''

# square 함수 정의
def square(n):
    return n ** 2

# 함수 호출하여 3과 4의 제곱 출력
result1 = square(3)
result2 = square(4)

print("3의 제곱은:", result1)
print("4의 제곱은:", result2)
