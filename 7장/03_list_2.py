'''
    작성일 : 2023년 10월 18일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  list 에서 사용 가능한 함수
'''

#리스트 생성
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("num_list", num_list)

print("num_list 의 길이 : ", len(num_list))
print("num_list 의 최대값 : ", max(num_list))
print("num_list 의 최소값 : ", min(num_list))
print("num_list 의 항목의 합계 : ", sum(num_list))
print("num_list 의 항목의 평균 : ", sum(num_list) / len(num_list))
print("num_list 의 항목의 0이 아닌 원소가 있는가 : ", any(num_list))