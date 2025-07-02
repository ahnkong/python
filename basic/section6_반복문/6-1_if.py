# -------------------------------------------------
# SECTION 6-1 : if
# -------------------------------------------------


weather = input("오늘 날씨는 어때욧\n")

if weather == "비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else : 
    print("준비물 필요 없어요!")    


temp = int(input("기온은 어때요?\n"))
if 30 <= temp :
    print("너무 더워요!! 에어컨!!")
elif 10<=temp and temp <30 :
    print("좋은 날씨네용")
elif 0 <= temp < 10 :
    print("너무 추춰요!. 나가지 말죠 우리!")


