print(1+1)
print(2**3)

print(5%3) #나머지
print(10//2) #몫

print(3 == 3) #true
print(4 == 2) #false
print(3 + 4 == 7) #true

print(1 != 3) #1은 3과 같지 않다.
print(not 1 != 3) #false

print(( 3 > 0) and ( 3 < 5 )) #3은 0보다 크고 5보다 작댜
print(( 3 > 0) & ( 3 < 5)) #3은 0보다 크고 5보다 작댜

print( (3>0) or (3<5)) #3은 0보다 크거나 5보다 작댜
print( (3>0) | (3<5)) #3은 0보다 크고 5보다 작댜

print(5 > 4> 3)

print(2+3+4)
print((2+3)*4)  



print("-------------------------------")
number = 2 + 3 * 4  #14
print(number)

number += 2  #number = number + 2
print(number)

number *= 2  #number * number + 2
print(number)
number /= 2  #number / number + 2
print(number)
number -= 2  #number - number + 2
print(number)

number %= 2 #0



print("-------------------------------")
print(abs(-5)) 
print(pow(4,2)) # 4*4 제곱
print(max(5, 12))
print(min(5,12))
print(round(3.14)) #반올림
print(round(4.99))

from math import *
print(floor(4.19)) #내림 4
print(ceil(3.14)) #올림 4

print(sqrt(16)) # 제곱근 4


print("-------------------------------")
from random import *

#난수 뽑기!!

print(random())  #0.0~1.0 미만의 임의의 값 생성
print(random())
print(random()) 
print(random() * 10)   #0.0~10.0 미만의 임의의 값 생성
print(int(random() * 10))   #0.0~10.0 미만의 임의의 값 생성 + 정수형
print(int(random() * 10))   #0.0~10.0 미만의 임의의 값 생성 + 정수형
print(int(random() * 10) + 1)   #1~10 미만의 임의의 값 생성 + 정수형
print(int(random() * 10) + 1) #1~10 미만의 임의의 값 생성 + 정수형



# 로또 난수 번호 생성
print(int(random() * 45) +1) #1~45 이하의 임의의 값 생성
print(int(random() * 45) +1) #1~45 이하의 임의의 값 생성
print(int(random() * 45) +1) #1~45 이하의 임의의 값 생성
print(int(random() * 45) +1) #1~45 이하의 임의의 값 생성
print(int(random() * 45) +1) #1~45 이하의 임의의 값 생성
print(int(random() * 45) +1) #1~45 이하의 임의의 값 생성

#범위 지정
print("범위 지정")
print(randrange(1, 45)) #1~45 미만의 임의의 값 생성

print(randrange(1, 46)) #1~45 이하의 임의의 값 생성
print(randrange(1, 46)) #1~45 이하의 임의의 값 생성
print(randrange(1, 46)) #1~45 이하의 임의의 값 생성
print(randrange(1, 46)) #1~45 이하의 임의의 값 생성
print(randrange(1, 46)) #1~45 이하의 임의의 값 생성
print(randrange(1, 46)) #1~45 이하의 임의의 값 생성


print(randint(1, 45)) # 1~45 이하의 임의의 값 생성, 양쪽 끝도 포함
print(randint(1, 45)) # 1~45 이하의 임의의 값 생성, 양쪽 끝도 포함
print(randint(1, 45)) # 1~45 이하의 임의의 값 생성, 양쪽 끝도 포함
print(randint(1, 45)) # 1~45 이하의 임의의 값 생성, 양쪽 끝도 포함
print(randint(1, 45)) # 1~45 이하의 임의의 값 생성, 양쪽 끝도 포함
print(randint(1, 45)) # 1~45 이하의 임의의 값 생성, 양쪽 끝도 포함


print("-------------------------------")
#퀴즈
#월 4회 스터디 3번 온라인/1번은 오프라인
    # 조건1 : 랜덤 => randRange, randInt
    # 조건2 : 월별 날짜가 다르므로 최소 일수인 28일자로 randInt
    # 조건3 : 매월 1~3일은 스터디 준비 해야하므로 제외  4,28

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("오프라인 스터디 모임 날짜는 ")


for mm in month :
    date = randint(4, 28)
    sentance = str(mm) +"월" + str(date) + "일로 선정되었습니다."
    print(sentance)



# month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# print("오프라인 스터디 모임 날짜는:")

# for m in month:
#     offline_day = randint(4, 28)  # 각 월마다 다른 날짜 뽑기
#     sentance = str(m) + "월: " + str(offline_day) + "일로 선정되었습니다."
#     print(sentance)