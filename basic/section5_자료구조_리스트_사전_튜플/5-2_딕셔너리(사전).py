

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
