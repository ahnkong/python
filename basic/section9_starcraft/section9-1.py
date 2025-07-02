# 일반 유닛 : move
    # 일반 유닛 공격 : attack, damaged
# 공중 유닛 : fly
    # 공중 유닛 공격 : move(일반 유닛거 재정의)







#---------------------
# 일반 유닛
#---------------------
class Unit:
    def __init__(self, name, hp, speed): #self-> ahn 변수명이므로 바꾸면 된댜
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다.[속도{2}]"\
              .format(self.name, location, self.speed))


#---------------------
# 일반 유닛 공격
#---------------------
class AttackUnit(Unit) : #일반 유닛을 상속받음 class명(상속받을 class)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) #name, hp 상속받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))



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
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# # 벌처 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 :  공중 유닛, 체력도 좋고, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


# # 건물
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location):
#         pass #일단 패스 그냥 넘어가는거 continue임

# # 서플라읻 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over() :
#     pass


# game_start()
# game_over()


#-----------------------------------
# super
#-----------------------------------
# 건물
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) #초기화해줄때,
        super().__init__(name, hp, 0)  # super로 초기화 해줄때는, self안써쥼
        self.location = location
