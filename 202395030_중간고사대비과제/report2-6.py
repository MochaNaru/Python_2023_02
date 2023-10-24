'''
    작성일 : 2023년 10월 24일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : p 195 7.1 문제
'''

num_list = [100, 200, 300, 400, 500, 600, 700, 800]
high = 6
low = 3

# 리스트의 각 표현식을 실행하고 결과를 출력
print(num_list[high])         # (high) 6번째 수
print(num_list[high - 2])     # 6번째 - 2 번째 수
print(num_list[high - low])   # high - low 6 - 3 번째 수
print(num_list[-1])           # -1 번째 수 (가장 마지막 수)
print(num_list[-low])         # -3 번째 수
print(num_list[2*3])          # 6번째 수
print(num_list[2] * 3)        # 2번째 수(200)을 3번 반복한 리스트
print(num_list[5%4])          # 5를 4로 나눈 1 번째 리스트 출력
print(len(num_list))          # 리스트의 길이 출력
print(min(num_list))          # 제일 작은수 출력
print(max(num_list))          # 제일 큰수 출력
print(num_list[:3])           # 처음부터 3번째 까지의 수 출력
print(num_list[1:5])          # 2번째 요소부터 5번째 요소까지 출력
print(num_list[-1:-5:-1])     # 뒤에서부터 1번째 요소 부터 5번째 요소 까지 역순으로 출력
print(num_list[-5:-1])        # 뒤에서부터 5번째 요소 부터 1번째 요소까지 출력
