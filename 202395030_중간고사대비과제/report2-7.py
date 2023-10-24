'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 195 7.2 문제
'''

list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

# 이중 for 루프를 사용하여 각 원소를 곱하고 출력
for num1 in list1:  # list1의 각 원소에 대해 반복
    for num2 in list2:  # list2의 각 원소에 대해 반복
        result = num1 * num2  # 두 원소를 곱한 결과 계산
        print(f"{num1} * {num2} = {result}")  # 결과 출력
