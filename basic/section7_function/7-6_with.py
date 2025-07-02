import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

#with문을 쓰면, 매번 close()종료해줄 필요없이, 자동으로 종료해준다.
#그렇기때문에 더 수월하다


# study.file에 작성
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")




# study.file을 읽어오기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())