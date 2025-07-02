# print("나누기 전용 계산기 입니다.")
# num1 = int(input("첫번째 숫자를 입력하세요 : "))
# num2 = int(input("두번째 숫자를 입력하세요 : "))
# print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))





#-------------------------------------------------------
#
#-------------------------------------------------------

# try :
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# #예외 문자열이 들어온다면
# except ValueError:
#     print("에러에러!! 잘못된 값을 입력하셨습니다!")


# #예외 0으로 나누게 된다면
# except ZeroDivisionError as err:
#     print(err)




try :
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : "))) #nums[0]
    nums.append(int(input("첫번째 숫자를 입력하세요 : "))) #nums[1]
    # nums.append(int(nums[0]/nums[1]))                  #nums[2]
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
#예외 문자열이 들어온다면
except ValueError:
    print("에러에러!! 잘못된 값을 입력하셨습니다!")


#예외 0으로 나누게 된다면
except ZeroDivisionError as err:
    print(err)


#예외) 수식을 까먹었을떄
except Exception as err : 
    print("알 수 없는 에러가 발생했습니당!")    
    print(err)