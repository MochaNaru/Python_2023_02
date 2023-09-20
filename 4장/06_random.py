'''
    작성일 : 2023년 09월 20일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  선택문 if ~ else
            random 을 이용한 가위바위보 게임.
            
            randim 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 -> 가위
            1 -> 바위
            2 -> 보
'''

import random

print("가위바위보 게임을 시작합니다.")
num = random.randrange(3) # randrange(3)로 0,1,2 생성

#가위 바위 보 출력

if num == 0 :
    print("가위")

if num == 1 :
    print("바위")
    
if num == 2 :
    print("보")
    