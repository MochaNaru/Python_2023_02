'''
    작성일 : 2023년 10월 04일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  터틀을 이용하여 별을 그리기
            교재 131 페이지
'''

import turtle as t

t.shape("turtle")

t.penup()
t.goto(-50, -50)
t.pendown()

i = 0

while i < 5: #종료조건
    t.forward(300) #300만큼 이동
    t.right(144) #144도 만큼 꺾는다
    i += 1 #i변수에 1을 더한다
t.mainloop()  #종료해도 창이 안 닫히게 한다