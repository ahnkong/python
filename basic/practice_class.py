class Unit :
    def __init__(self):
        print("Unit생성자")


class Flyable :
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit): 
    def __init__(self):
        # super().__init__() #다중상속시 super로 초기화 해주면, 앞에있는 class만 초기화 하게 됨
        Unit.__init__(self) # 따라서, 각각의 class를 초기화 해주면 된다.
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()