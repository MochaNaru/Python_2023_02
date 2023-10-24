'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 143 5.7 세자리의 암스트롱수를 출력하는 프로그램
'''

def find_armstrong_numbers():
    armstrong_numbers = []  # 암스트롱 수를 저장할 빈 리스트 생성
    for num in range(100, 1000):  # 세 자리 정수 범위 (100 이상, 999 이하)
        # 각 자릿수를 분리하여 각 자릿수를 세제곱한 값을 합산
        digit1 = num // 100  # 백의 자릿수 추출
        digit2 = (num // 10) % 10  # 십의 자릿수 추출
        digit3 = num % 10  # 일의 자릿수 추출
        total = digit1 ** 3 + digit2 ** 3 + digit3 ** 3

        # 합산한 값이 입력된 수와 같으면 암스트롱 수
        if total == num:
            armstrong_numbers.append(num)

    return armstrong_numbers

# 모든 세 자리 암스트롱 수를 찾아 출력
armstrong_numbers = find_armstrong_numbers()
print("세 자리의 암스트롱 수:", armstrong_numbers)