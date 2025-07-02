#---------------------------------------------------
# 8-4) pickle
# 프로그램상에서 사용하는 데이터를 파일로 저장하는거
# 이 데이터를 파일로 만들고, 이 파일을 또 누군가가 가져가서 코딩하게
#---------------------------------------------------
import pickle
# profile_file = open("profile.pickle", "wb") # wb = write + binary타입
# profile = {"이름":"박보검", "나이" : 28, "취미":["런닝", "책읽기", "피아노"]} #사전 형태
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 잇는 정보를 file에 저장
# profile_file.close()



profile_file = open("profile.pickle", "rb") # rb = read + binary타입
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기

print(profile)
profile_file.close()