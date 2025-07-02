# -------------------------------------------------
# SECTION 6-1 : if
# -------------------------------------------------


# weather = input("오늘 날씨는 어때욧\n")

# if weather == "비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else : 
#     print("준비물 필요 없어요!")    


# temp = int(input("기온은 어때요?\n"))
# if 30 <= temp :
#     print("너무 더워요!! 에어컨!!")
# elif 10<=temp and temp <30 :
#     print("좋은 날씨네용")
# elif 0 <= temp < 10 :
#     print("너무 추춰요!. 나가지 말죠 우리!")


# -------------------------------------------------
# SECTION 6-2 : for
# -------------------------------------------------
# for wating_no in [0, 1, 2, 3, 4]:
    # print("대기번호 : {0}".format(wating_no))


#randrange
# for wating_no in range(1, 6): #0,1,2,3,4
#     print("대기번호 : {0}".format(wating_no))



# starbucks = ["아이언맨", "토르", "그루트", "스파이더맨"]
# for customer  in starbucks :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))




# -------------------------------------------------
# SECTION 6-3 : while
# -------------------------------------------------

# customer = "토르"
# index = 5
# while index >=1 :
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분 되었습니다.")


# customer = "아이언맨" #무한 루프
# index = 1
# while True :
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회 ".format(customer, index))
#     index +=1


# customer = "그루트"
# person ="Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?? ") 



# -------------------------------------------------
# SECTION 6-4 : continue, break
# -------------------------------------------------

# absentKids = [2,5] #결석하면 다음 번호 진행
# no_book = [7] #책은 꼭 있어야해
# for student in range(1, 11) :
#     if student in absentKids: 
#         continue #이거 만나면 밑에거 skip
#     elif student in no_book :
#         print("책없으면 수업 못해. 오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
#         break
#     print("{0}, 일어나서 책 읽어봐".format(student))


# -------------------------------------------------
# SECTION 6-5 : 한줄 for
# -------------------------------------------------
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함. -> 101 102 103 104
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)


# #학생 이름을 길이로 변환
# student =["ironman", "Thor", "Iamgroot"]
# # student =[len(i) for i in student]
# print(student)


# #학생 이름을 대문자로 변환
# student = [i.upper() for i in student]
# print(student)



# -------------------------------------------------
# SECTION 6-6 : 퀴즈
# 50명 승객과 매칭기회가 있다. 총 탑승 승객수 구해야함.
# 조건1 : 승객별 운행 소요 시간 5분 ~ 50분 사이의 난수로 정해야함.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭 해야함.

# (출력문 예제)
# [ㅇ] 1번째 손님 (소요시간: 15분)
# [] 2번째 손님 (소요시간: 50분)
# [ㅇ] 3번째 손님 (소요시간: 5분)
# ...
# [] 50번째 손님 (소요시간: 16분)
# 총 탑승 승객 : 2명
# -------------------------------------------------
# from random import *

# customer = range(0, 51)
# time = int((random() * 15) + 5)
# print(time)
# cnt = 1

# for i in range(1, 51) : #1~50 이라는 수(승객)
#     time = randrange(5, 51)
#     if 5 <= time <= 15 : #5분~15분 이내의 손님, 탑승 승객 수 증가
#      print("[o] {0}번째 손님 (소요시간: {1}분)".format(i, time))
#      cnt += 1
#     else: # 매칭 실패한 경우
#          print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))
       
# print("총 탑승 승객 : {0}명".format(cnt))


#-------------------------------
from random import *
cnt = 0

for i in range(1, 51) : #1~50까지의 승객수 동안 반복
    time = randrange(5, 51) #5분에서 50분 까지의 난수
    if 5 <= time <= 15 :
        cnt += 1
        print("[ㅇ] {0}번째 손님 (소요시간: {1}분)".format(i, time))
    else : #매칭 실패
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i, time))

print("총 탑승 승객 : {0}명".format(cnt))