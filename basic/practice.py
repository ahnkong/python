# print(5)
# print (-10)
# print(3.14)
# print(1000)
# print(3+5)
# print(3*10)
# print(3*(3+1))
# print("풍선")
# print(5>10)
# print(True)
# print(not True)
# print(not (5> 10))


# 변수

# name = "연탄이"
# animal  = "강아지"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

name = "콩이"
animal  = "강아지"
age = 4
hobby = "인형 물어뜯기"
is_adult = age >= 3


# print("우리집 강아지의 이름은 연탄이에요")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요??? true")

# print("우리집" + animal + "의 이름은 " + name + "에요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")
# print(name + "는 어른일까요???" + str(is_adult))


# print("우리집" + animal + "의 이름은 " + name + "에요")
# hobby = "공놀이"


# 문자열 붙이기
# +가 아닌 , 로도 문자열을 이을수 있음
# print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")
# print(name, "는 ", age, "살이며,", hobby, "를 아주 좋아해요")
# print(name, "는 ", age, "살이며,", hobby, "를 아주 좋아해요", sep="")
# print(name + "는 어른일까요???" + str(is_adult))


#quiz
station = ["사당", "신도림", "김포공항"]

for i in station :
    print(i, "행 열차가 들어오고 있습니다.")
