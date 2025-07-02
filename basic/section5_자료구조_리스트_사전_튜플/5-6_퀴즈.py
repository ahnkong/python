
# -------------------------------------------------
# SECTION 5-6 : 퀴즈
# -------------------------------------------------

# 조건1 : 편의상 댓글은 20명이 작성, 아이디는 1~20
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random모듈의 shiffle과 sample을 활용

#출력예제
# -- 당첨자 발표--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다.--

#활용예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) #무작위로 섞기
# print(lst)
# shuffle()은 리스트 순서를 섞고, sort()는 정렬해요. 
# sample()은 리스트에서 무작위로 여러 개를 중복 없이 선택할 때 사용해요.

from random import *
users = range(1,21) # 1부터 20까지 숫자 생성
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(sample(users, 4)) #lst에서 1개를 무작위로 뽑겟댜

print("---당첨자 발표 ---")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:])) #1,2,3에 있는 위치의 아이들가져옴!
print("---축하합니다. ---")

# print(random() * 10)   #0.0~10.0 미만의 임의의 값 생성
id = int(random() * 20)
print(id)
