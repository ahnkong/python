#finally 
#정상이든, 예외든 무조건 마지막에는 실행되어야 함.

class BignumberError(Exception):
    def __init__(self, msg):
        self.msg = msg



    def __str__(self):
        return self.msg

try : 
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("입력값 : {0},{1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하셨습니다. 한자리 숫자만 입력하세요")



except BignumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)


finally:
    print("계산기를 이용해 주셔서 감사합니다.")