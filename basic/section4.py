# sentence = "나는 소년입니다."
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)


# sentence3=""" 
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


#슬라이싱
jumin = "920922-1234567" 
print("성별 : " + jumin[7]) #2000년대생 이전, 남:1, 여:2 2000년대생 이후 남:3, 여:4
print("출생년도 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 :" + jumin[0:6]) #처음부터 ~6직전까지
print("생년월일 :" + jumin[:6]) #처음부터 ~6직전까지


print("주민번호 뒷자리 : " +jumin[7:14]) #7번째부터 ~ 끝까지
print("주민번호 뒷자리 : " +jumin[7:])

print("뒤 7자리 (뒤에부터 ) : " + jumin[-7:]) #뒤에서부터 7번째수 ~ 끝까지


##문자열 처리 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #python 0번째가 대문자가 맞아? t
print(len(python))
print(python.replace("Python", "Java")) #문자열 바꾸기

index = python.index("n") #몇번쨰인지 확인
print(index)


index = python.index("n", index +1) #start위치인 5+1부터 => 6부터 n찾기
print(index)

# print(python.index("Java")) # 오류-> 프로그램 종료
print(python.find("Java")) #-1 출력 -> 이후 계속 출력

print(python.count("n")) # 몇번 나오나유


