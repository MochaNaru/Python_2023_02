'''
    작성일 : 2023년 10월 18일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  list 의 객체 생성과 참조
'''

fruits_1 = ['사과', '산딸기', '바나나']

#실제 값을 복사하는게 아니라 리스트의 저장 위치(주소)가 복사된다.
fruits_2 = fruits_1

print("fruits_1 : ", fruits_1)
print("fruits_2 : ", fruits_2)

fruits_2[1] = '망고' # fruits_2의 1번지 과일을 망고로 바꾸면

print("fruits_1 : ", fruits_1) #모두 1번지 내용이 망고로 바뀐다.
print("fruits_2 : ", fruits_2)

#주소 확인 => 메모리 위치 정보 알아보기 id()
print("fruits_1의 id ", id(fruits_1))
print("fruits_2의 id ", id(fruits_2))

#리스트 내용 복제하기 list()함수 사용
fruits_2 = list(fruits_1) #내용 복제(배정)
print(":: 내용 복제후 1 ::")
print("fruits_1 : ", fruits_1)
print("fruits_2 : ", fruits_2)

print("fruits_1의 id ", id(fruits_1))
print("fruits_2의 id ", id(fruits_2))

#내용 복제 2
fruits_3 = fruits_1[:]

print(":: 내용 복제후 2 ::")
print("fruits_1 : ", fruits_1)
print("fruits_3 : ", fruits_3)

print("fruits_1의 id ", id(fruits_1))
print("fruits_3의 id ", id(fruits_3))

fruits_3[0] = '수박' #0번지 내용을 수박으로 바꾼다
print(":: fruits_3의 0번지 내용을 수박으로 바꾼 후 ::")
print("fruits_1 : ", fruits_1)
print("fruits_3 : ", fruits_3)