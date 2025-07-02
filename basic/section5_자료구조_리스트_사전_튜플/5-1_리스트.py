
# -------------------------------------------------
# SECTION 5-1 : 리스트
# -------------------------------------------------


# # 지하철 칸별로 10명, 20명, 30명
# subway1= 10
# subway2= 20
# subway3= 30
# subway4= 40


# subway = [10, 20, 30, 40]
# print(subway)


# subway = ["차은우","박보검", "송강"]
# print(subway)



# #보검이 몇 번재 칸에 타고 있는가
# print(subway.index("박보검"))

# # 우빈이 추가 = 
# # appned는 맨 뒤에 붙는가
# subway.append("안우빈")
# print(subway)

# # 민정이를 차은우와 보검이 파이에 태움
# subway.insert(1, "안민정")
# print(subway)


# #한명씩 뒤에서 빼보기
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)


# # 같은 이름의 사람 몇명 있는지 확인하기
# subway.append("박보검")
# print(subway)
# print(subway.count("박보검"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)


# #순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)


# # 리스트 : 다양한 자료형 함께 사용 가능
# num_list = [5,2,4,3,1]
# mix_list = ["박보검", 20, True]
# # print(mix_list)

# # 리스트 + 리스트
# num_list.extend(mix_list)
# print(num_list)



# -------------------------------------------------
# SECTION 5-2 : 딕셔너리(사전)
#   키 중복 : X
# -------------------------------------------------

# cabinet ={3:"안민정", 100:"안우빈"} #열쇠 3, 100
# print(cabinet[3]) #키에 따른 밸류
# print(cabinet[100])

# print(cabinet.get(3)) 
# print(cabinet[5]) #오류면 index처럼 에러나고 이후 종료
# print(cabinet.get(5)) # 오류나도 none이라고 뜨고, 이후 실행
# print(cabinet.get(5, "사용가능")) # 오류나면 "사용가능"이라고 뜨고, 이후 실행
# print("hi")

#키의 존재 여부
# print(3 in cabinet) # true
# print(5 in cabinet) # false

# cabinet ={"A-3":"안민정", "B-100":"안우빈"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "박보검" #이렇게 위에서 선언한 사전을 이후에 덮어쓰면, 박보검이가 a-3쓰게 됨
# cabinet["c-300"] = "차은우"
# print(cabinet)


# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key,.value둘다 출력
# print(cabinet.items())


# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)


# -------------------------------------------------
# SECTION 5-3 : 딕셔너리(사전)
#   속도가 리스트보다 빠르다
#   변경되지 않는 목록을 사용할 때 빠르다. 
#   ( ) 사용
# -------------------------------------------------

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])          

# # menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) =  ("차은우", "24", "잠자기")
# print(name, age, hobby)


# -------------------------------------------------
# SECTION 5-4 : 세트(집합)
#  중복안됨. 순서 없음
# -------------------------------------------------
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)

# print(java.intersection(python))


# #합집합 (java와 python을 할 수 있는 모든 개발자)
# print(java | python)
# print(java.union(python))


# #차집합 (java는 할 수 있지만, python을 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))


# # 파이썬 할 줄 아는 사람이 늘어남
# python.add("지예은")
# print(python)


# # 김태호 java 안한지 오래돼서 까묵음
# java.remove("김태호")
# print(java)



# -------------------------------------------------
# SECTION 5-5 : 자료구조의 변경
# -------------------------------------------------

# menu ={"커피", "우유", "주스"} #set
# print(menu)
# print(menu, type(menu)) #무슨 타입인지 알려줌



# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# #{'우유', '커피', '주스'} <class 'set'>
# #['우유', '커피', '주스'] <class 'list'>
# #('우유', '커피', '주스') <class 'tuple'>

# menu = set(menu)
# print(menu, type(menu)) #{'우유', '커피', '주스'} <class 'set'>



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
