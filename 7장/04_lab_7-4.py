'''
    작성일 : 2023년 10월 18일
    작성자 : 202395930 컴퓨터공학부 정성욱
    설명 :  도시의 인구 자료에 대한 슬라이싱
'''

#list를 생성
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]

#서울과 인천의 인구수를 출력
print("서울인구 : ", population[1]) #리스트의 2번째 항목 출력 
print("인천인구 : ", population[-1]) #리스트의 마지막 항목 출력

#도시 이름을 리스트로 출력
cities = population[0::2] #리스트 0부터 2칸씩 가져와서 변수에 담는다
print("도시 리스트 : ", cities)

#리스트안의 도시 인구를 합하여 출력
pops = population[1::2] #2번째 부터 2칸씩 가져와서 변수에 담는다
print("인구의 합 : ", sum(pops))