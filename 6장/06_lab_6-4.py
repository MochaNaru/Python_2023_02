'''
    작성일 : 2023년 10월 11일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min 을 입력받아 최대, 최소값을 찾아 돌려주는 함수
    
    (함수)
            5) 두 값을 전달받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다. max(), min()
            7) 값을 돌려준다.
    
    (메인)
        1. 무한반복
            1) 랜덤으로 10 ~ 99까지 10개의 수를 리스트로 생성
            2) 생성딘 리스트를 출력
            3) 사용자로부터 최대값을 알고싶은지 최소값을 알고싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min 
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8) 돌려받은 최대값 또는 최소값을 출력한다. 
'''

def getMinMax(mylist, method = 'max') : # 값을 전달받은 함수를 생성
    minValue = 999999999999999999
    maxValus = -minValue
    
    if method == 'max' : # 리스트에서 최대값을 찾는 조건식
        for Value in mylist :
            if Value > maxValus :
                maxValus = Value;
        return maxValus
    elif method == 'min' : # 리스트에서 최소값을 찾는 조건식
        for Value in mylist :
            if Value < minValue :
                minValue = Value;
        return minValue
    else :
        print("illegal method")


while (True) : #무한반복

    import random #랜덤 함수
        
    mylist = random.sample(range(10, 100), 10) #10 ~ 99 사이의 숫자로 10개의 숫자를 생성
    print(mylist) # 리스트를 출력

    s = input("최대값을 원하면 max, 최솟값을 원하면 min을 입력하시오 : ") # 사용자에게 최소값 / 최대값을 물어본다
    print(getMinMax(mylist, s)) #결과를 출력
