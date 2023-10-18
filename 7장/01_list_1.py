'''
    작성일 : 2023년 10월 18일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  list 만들기
'''

#과일 리스트 만들기
fruits = ['사과', '산딸기', '바나나']
print("과일목록 : ", fruits)

#귤 추가 => append 사용 (마지막에 추가)
fruits.append('귤')
print("과일 목록(귤 추가)", fruits)

fruits.append('포도')
print("과일 목록(포도 추가)", fruits)

#복숭아 추가 => + 연산자 사용
fruits = fruits  + ['복숭아']
print("과일 목록(복숭아 추가)", fruits)

num = [1, 2, 3] + [4, 5, 6]
print("숫자 리스트", num)

# * 연산자
num = [1, 2, 3] * 3
print("숫자 리스트 * 3", num)

# in 연산자 => 포함 되는가? 
print("과일 목록에 복숭아가 있나요?", '복숭아' in fruits)

# index 를 사용하여 list 의 항목에 접근하기

#과일 list 의 갯수
print("과일 의 갯수는? ", len(fruits))

#과일 list 중 제일 첫 번째 과일은? 
print("과일 중 제일 좋아하는 과일은?", fruits[0]) 

#과일  list중 제일 마지막 과일은?
print("과일 중 제일 마지막 과일은? ", fruits[-1])

#과일 중 가장 큰 과일은?
print("과일중 가장 큰 과일은?(사전식 순서)", max(fruits))

#과일중 가장 작은 과일은?
print("과일중 가장 작은 과일은?(사전식 순서)", min(fruits))

# 정렬
fruits.sort() #오름차순
print("오름차순 정렬 : ", fruits)

fruits.sort(reverse=True) #내림차순
print("내림차순 정렬 : ", fruits)

#list  를 원하는 모양으로 자르기
print("과일 목록 : ", fruits)
print("과일 리스트중 2번 3번 4번 과일을 찾고싶어요 : ", fruits[1:4]) #1번지 부터 4번지 앞까지
print("과일 리스트중 1~3번 과일을 찾고싶어요 : ", fruits[0:3]) #0번지 부터 3번지 앞까지
print("과일 리스트중 1~3번 과일을 찾고싶어요 : ", fruits[:3]) #1번지 부터 4번지 앞까지
print("과일 리스트중 3번 과일부터 마지막 과일을 찾고싶어요 : ", fruits[2:]) #3번지 부터 마지맏까지

#처음부터 끝까지 2씩 증가하면서 찾기
print("과일 리스트중 처음부터 2씩 증가하면서 과일을 찾고싶어요 : ", fruits[::2])
print("과일을 거꾸로 출력", fruits[::-1])

#리스트의 원소 값을 자유롭게 조작해 보자.

print()

print("과일목록 : ", fruits)

#원하는 위치에 '두리안' 추가 => insert() 메소드 사용
fruits.insert(3, "두리안")
print("과일목록 : ", fruits)

#위치찾기 => index() 메소드 사용
print("사과의 위치는? ", fruits.index('사과'))

#사과를 마지막에 추가
fruits.append('사과')
print("과일목록(사과를 마지막에 추가) : ", fruits)

#사과의 개수 => count() 메소드 사용
print("사과의 개수는? ", fruits.count('사과'))

#list 의 항목 삭제

print()

# 사과 삭제 remove() 메소드 사용 : 삭제할 항목 지정
fruits.remove('사과') #처음 만나는 사과만 삭제
print("과일목록(사과 삭제후 리스트) : ", fruits)

#항목삭제 => pop() 메소드
fruits.pop() #마지막 항목 삭제
print("과일목록(마지막 과일 삭제) : ", fruits)

#del() 키워드 => 포도 삭제
del fruits[0] #0번지 항목 삭제
print("과일목록(0번지 항목 삭제후 리스트) : ", fruits)
