'''
    작성일 : 2023년 09월 20일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  선택문 if ~ else
            random 을 이용한 가위바위보 게임.
            
            randim 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 -> 가위
            1 -> 바위
            2 -> 보
            
            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''

import random

print("가위바위보 게임을 시작합니다.")

player1 = input("player1 의 이름 : ")
player2 = input("player2 의 이름 : ")

num1 = random.randrange(3) #첫번째 플레이어의 번호 
num2 = random.randrange(3) #두번째 플레이어의 번호

#가위 바위 보 출력

print(player1," : ", end=' ')

if num1 == 0 :
    print("가위")

if num1 == 1 :
    print("바위")
    
if num1 == 2 :
    print("보")

print(player2," : ", end=' ')

if num2 == 0 :
    print("가위")

if num2 == 1 :
    print("바위")
    
if num2 == 2 :
    print("보")
    
#승자 판단하여 출력
if num1 == num2 :
    print("무승부입니다.")
else :
    if  (num1 == 1 and num2 == 0 ) and (num1 == 2 and num2 == 1) and (num1 == 0 and num2 == 2) :
        print(f"{player1}의 승리")
    else :
        print(f"{player2}의 승리")