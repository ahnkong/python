# 일반 유닛 : move
    # 일반 유닛 공격 : attack, damaged
# 공중 유닛 : fly
    # 공중 유닛 공격 : move(일반 유닛거 재정의)



#---------------------
# 일반 유닛
#---------------------

from random import *


class Unit:
    def __init__(self, name, hp, speed): #self-> ahn 변수명이므로 바꾸면 된댜
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))


    def move(self, location) :
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도{2}]"\
              .format(self.name, location, self.speed))

    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))


#---------------------
# 공격 유닛 
#---------------------
class AttackUnit(Unit) : #일반 유닛을 상속받음 class명(상속받을 class)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #name, hp 상속받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
        

#마린
class Marrine(AttackUnit) :
    def __init__(self):
            AttackUnit.__init__(self, "마린", 40, 1, 5)

    
    #스팀팩 : 일정 시간 동안 공격 속도를 증가, 체력 40중 10 감소
    def stimpack(self) : 
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.(hp 10감소)".format(self.name))
        else : 
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


#탱크
class Tank(AttackUnit) :
        #시즈 모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
        #
        seize_developed =False #시즈모드 개발여부


        def __init__(self):
            AttackUnit.__init__(self, "탱크", 35, 1, 5)
            self.seize_mode = False


        def set_seize_mode(self):
            if Tank.seize_developed == False :
                return
            

            # 현재 시즈모드가 아닐 때
            if self.seize_mode == False:
                print("{0} : 시즈모드로 전환합니다.".format(self.name))
                self.damage *= 2
                self.seize_mode = True
            # 현재 시즈모드 일 때
            else :
                print("{0} : 시즈모드를 해제 합니다.".format(self.name))
                self.damage /= 2
                self.seize_mode =False

# 메딕 : 의무병, 공격력 X
# 파이어뱃 : 공격 유닛, 화염방사기
# 드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격X

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self, name, location):
         print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
               .format(name, location, self.flying_speed))
         


# 공중 유닛 공격 클래스
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상스피드는 0으로 처리
        Flyable.__init__(self, flying_speed)

    def move(self, location): #일반유닛의 move를 재정의
        # print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 레이스 
class Wraith(FlyableAttackUnit) :
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)


    def clocking(self) :
        if self.clocked == True: # 클로킹 모드 설정 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else :  #클로킹 모드 해제 => 모드 설정
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


 
def game_over():
    print("Player : gg")
    print("[Player] 님이 퇴장하셨습니다.")










#-----------------------------------------
# 실제 게임 시작
#-----------------------------------------
game_start()


# 마린 3개 생성
m1 = Marrine()
m2 = Marrine()
m3 = Marrine()


#탱크 2기 생성
t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1 = Wraith()


# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


# 전군 이동
for unit in attack_units:
    unit.move("1시")


# 탱크 시즈 모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료 되었습니다.")

#공격모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units :
    if isinstance(unit, Marrine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# 전군 공격
for unit in attack_units :
    unit.attack("1시")



# 전군 피해
for unit in attack_units :
    unit.damaged(randint(5, 21)) #공격은 랜덤으로 받음(5~20)


# 게임 종료
game_over()