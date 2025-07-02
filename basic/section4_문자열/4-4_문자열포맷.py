
# -------------------------------------------------
# SECTION 4-4 : 문자열 포맷
# -------------------------------------------------

# 방법 1 : %
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2 : .format()
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3 : .format(변수명=값)
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4 : f-string (Python 3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# -------------------------------------------------
# SECTION 4-5 : 탈출 문자
# -------------------------------------------------

# \\ : 역슬래시 출력
# print("C:\\Users\\Desktop\\pythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine")

# \b : 백스페이스 (앞 글자 삭제)
# print("Redd\bApple")

# \t : 탭 (들여쓰기 효과)
# print("Red\tApple")



# -------------------------------------------------
# SECTION 4-6 : 퀴즈
# -------------------------------------------------

# 퀴즈 : http://naver.com 사이트 별로 비밀번호 만들어 주는 프로그램 작성
# 규칙1 : http:// 부분 제외 => naver.com
# 규칙2 : 처음 만나는 점(.)이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 3자리 + 글자 갯수 + 글자내 'e'갯수 +"!"로 구성
#                         nav       5           1              1
# 예) 생성된 비밀번호 : nav51!


site = "http://google.com"
first = site[7:10]
print(first) #nav

second = len(site)
print(second) #16

third =site.count("e")
print(third) #5

fore = "!"


password = first + str(second) + str(third) + fore
print(password)  # 최종 결과 = "nav152"



# my_str = site.replace("http://", "") #규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] #규칙2   처음부터~my_str.index(".")직전까지
# # print(my_str)

# password =my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는{1} 입니다. " .format(site, password))