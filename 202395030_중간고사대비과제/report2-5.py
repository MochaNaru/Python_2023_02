'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 169 6.6 임의의 수를 입력으로 받은 다음 이 수가 소수인지 아닌지를 판단하는 함수 is_prime(n)을 작성
            만일 n이 소수이면 True, 그렇지 않으면 False를 반환하도록 하여라
'''

def is_prime(n):
    if n <= 1:  # 1 이하의 수는 소수가 아님
        return False
    if n == 2:  # 2는 소수
        return True
    if n % 2 == 0:  # 짝수는 소수가 아님
        return False

    # 3부터 n의 제곱근까지의 홀수로 나누어보며 소수 판단
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:  # n이 i로 나누어 떨어지면 소수가 아님
            return False

    return True

# 사용자로부터 수 입력 받기
number = int(input("정수를 입력하세요: "))

# is_prime 함수를 호출하여 소수 여부 판단
result = is_prime(number)

# 결과 출력
if result:
    print(f"{number}는 소수입니다.")
else:
    print(f"{number}는 소수가 아닙니다.")
