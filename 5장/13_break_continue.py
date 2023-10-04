'''
    작성일 : 2023년 10월 04일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 : 반복을 제저하는 break continue 
            교재 137 페이지
'''

word = input("단어를 입력하세요 : ")

print(":: break1 ::")

for i in word :
    if i == "a" or i == "i" or i == "o" or i == "u" : #종료 조건
        break #종료
    else :
        print(i, end='') #내용을 출력
        
print()
        
print(":: break2 ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U']: #종료 조건
        break #종료
    else :
        print(i, end='')
        
print()

print(":: continue ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U']: 
        continue #반복의 시작으로 돌아간다. 아래 문장을 만날 수 없다.
    print(i, end='')