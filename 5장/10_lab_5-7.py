'''
    작성일 : 2023년 10월 04일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  단을 입력 받아 해당 단의 구구단을 출력하시오.
            교재 130 페이지
            
        문제 분석 : 1.원하는 단을 입력받는다. (num)
                    2. (count) 변수가 9가될때까지 반복을 시킨다.
                    3. 곱한 수를 출력한다.(num*count)
        
        필요한 변수 : num, count
'''

num = int(input("원하는 단의 숫자를 입력하세요 : ")) #원하는 단(정수)를 입력받음
count = 1 #단을 곱할 숫자변수 저장

while count <= 9 : #종료조건
    print(f"{num} * {count} = {num*count}") #곱한식을 출력
    count += 1 #카운트 변수에 1을 더함