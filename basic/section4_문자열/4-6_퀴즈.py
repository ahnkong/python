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