'''
    작성일 : 2023년 09월 13일
    작성자 : 학과 학번 이름
    설명 : 터틀 그리기
'''

import turtle as t #터틀 모듈을 사용하기 위한 준비
                   #turtle 클래스 객체를 t로 생성. (별명)
                   

t.shape('turtle')
t.speed(2)

#선 그리기

# t.forward(200) #200픽셀 이동


#t.mainloop() # 그림판 사라지지 않는다

# 삼각형 그리기
#t.forward(200) #200px 만큼 이동
#t.left(120) #왼쪽으로 120도 회전
#t.forward(200) #200px 만큼 이동
#t.left(120) #왼쪽으로 120도 회전
#t.forward(200) #200px 만큼 이동
#t.left(120) #왼쪽으로 120도 회전

for i in range(500):
    t.forward(200) #200px 만큼 이동
    t.left(144) #왼쪽으로 120도 회전 
    
t.mainloop()