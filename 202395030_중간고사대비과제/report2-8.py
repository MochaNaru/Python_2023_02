'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 196 7.7 
    fruit_list = ['banana', 'orenge', 'kiwi', 'apple'. 'melon'] 의 리스트가 존재한다
    1) 이 fruit_list 에서 가장 길이가 긴 문자열을 찾아서 출력하고 이 리스트에서 삭제하라
    이때 동일한 길이의 문자열이 있을경우 이들을 모두 삭제하라
    2) 이 fruit_list 와 for 제어문을 이용하여 각 문자열의 길이를 출력하라
 '''

print(" ::: 1번 문제 ::: ")

fruit_list = ['banana', 'orenge', 'kiwi', 'apple', 'melon']

# 가장 긴 문자열의 길이 계산
max_length = max(len(fruit) for fruit in fruit_list)

# 가장 긴 문자열 또는 동일한 길이의 문자열을 삭제하고 출력
fruit_list = [fruit for fruit in fruit_list if len(fruit) != max_length]

print("가장 긴 문자열 삭제 후:", fruit_list)

print()

print(" ::: 2번 문제 ::: ")

fruit_list = ['banana', 'orenge', 'kiwi', 'apple', 'melon']

# 각 문자열의 길이 출력
for fruit in fruit_list:
    print(f"{fruit}의 길이: {len(fruit)}")