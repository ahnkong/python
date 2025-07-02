# #마린 : 공격유닛, 군인. 총을 쏠 수 있음.
# name = "마린"
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))


# #탱크 : 공격 유닛, 탱크. 대포 쏠수 있음. 일반 모드 /시즈 모드
# tank1_name = "탱크"
# tank1_hp = 150
# tank1_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank1_name))
# print("체력 {0}, 공격력 {1}\n".format(tank1_hp, tank1_damage))


# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))





# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))


# attack(name, "1시", damage)
# attack(tank1_name, "1시", tank1_damage)
# attack(tank2_name, "1시", tank2_damage)


#유닛 클래스 생성
#---------------------------
# init = 생성자 / 
# 마린, 탱크 = 인스턴스 / 
# self.name, self.hp = 멤버변수
#---------------------------
class Unit:
    def __init__(self, name, hp): #self-> ahn 변수명이므로 바꾸면 된댜
        self.name = name
        self.hp = hp
        # self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0} 공격력{1}\n".format(self.hp, self.damage))


# # marine1 = Unit("마린", 40, 5) #ahn 빼고 적어주면 된다.
# # marine2 = Unit("마린", 40, 5) #ahn 빼고 적어주면 된다.
# # tank = Unit("탱크", 150, 35)


# # 레이스 : 공중 유닛, 비행기, 클로킹( 상대방에게 보이지 않음 )
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것( 빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True #외부에서 추가로  이름, hp, 데미지 였는데 추가한거
#         # 따라서, wraith1에는 이름 체력,데미지  이렇게 3개
#         # wraith2는 이름, 체력, 데미지, 클로깅  이렇게 4개
#             #레이스1에서는 클로킹 변수 사용못함.

# if wraith2.clocking == True :
#     print("{0} 는 현재 클로킹 상태입니다. ".format(wraith2.name))

#공격유닛
class AttackUnit(Unit) : #일반 유닛을 상속받음 class명(상속받을 class)
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) #name, hp 상속받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
        #self는 자기 자신, 클래스 내에서 메서드 안에서 self를 항상 써줌
        #self.000해서 자기 자신의 변수에 접근
        #.format(self.name, location, self.damage) 여기서
            # self.name 은  init에 있는 거
            # self.damage
            # location -> 인자로 전달받은거
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))



# 메딕 : 의무병, 공격력 X




#파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25) 



# 드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격X

# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


    def fly(self, name, location):
         print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
               .format(name, location, self.flying_speed))
         


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사. 강력
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")



#