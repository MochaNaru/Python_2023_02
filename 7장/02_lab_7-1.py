'''
    작성일 : 2023년 10월 18일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  입력을 받아 맛있는 과일의 리스트를 만들자.
    
    좋아하는 과일 5개를 입력받아 리스트를 저장한다.
    과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단한다.
    
    추가 = append() 메소드
    찾기 = in 연산자
'''

#빈 리스트 생성
fruits = []

#5번 반복하면서 과일 이름 입력 받아 리스트에 저장
for i in range(5) :
    fruits_name = input(str(i+1) + ". 좋아하는 과일의 이름을 입력 : ")
    fruits.append(fruits_name)
    
print("과일 리스트 : ", fruits)

#찾고싶은 과일을 입력받아서 if 조건문으로 찾아주기
favo_fruits = input("찾고싶은 과일의 이름을 입력하세요.")

if favo_fruits in fruits :
    print(f"{favo_fruits}은(는) 리스트에 있습니다.")
    
else :
    print(f"{favo_fruits}은(는) 리스트에 없습니다.")