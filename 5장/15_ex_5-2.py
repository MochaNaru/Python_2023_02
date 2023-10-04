'''
    작성일 : 2023년 10월 04일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  두 수를 입력 받아 
            1. 두 수 사이의 합계 출력하기
            2. 두 수 사이의 짝수의 합계 출력하기
            
            심화문제 5.2, 141 페이지
'''

num1 = int(input("첫 번째 숫자를 입력해주세요 : ")) #숫자 1을 입력받는다.
num2 = int(input("두 번째 숫자를 입력해주세요 : ")) #숫자 2을 입력받는다.

if num1 < num2 :
    #작은 수
    start = num1
    #큰 수
    end = num2
else :
    #작은 수
    start = num2 
    #큰 수
    end = num1

print(":: 두 수 사이의 합계출력 ::")

#변수 초기화
count = start
sum = 0
total = 0

while count <= end : #반복 조건
    sum += count #합계에 count(start)를 더한다
    count += 1 #count(start)를 1증가 시킨다

print("두 수 사이의 합은 ", sum)

print() #줄바꿈
print(":: 두 수 사이 짝수의 합계출력 ::")
count = start

while count <= end : #반복 조건
    if count % 2 == 0 : #짝수인지 아닌지 판단
        total += count #짝수가 맞다면 total에 숫자를 추가
    count += 1 #판단과 별개도 숫자를1 증가
print("두 수 사이 짝수의 합은 ", total) #결과출력