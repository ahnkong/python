#---------------------------------------------------
# 8-3) 파일입출력
#---------------------------------------------------
score_file = open("score.txt","w", encoding="utf8") #w = 쓰기 위한 목적
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# #파일 쓰기 w
score_file=open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()


# #파일 읽어오기 r
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

    # 몇줄인줄 알때
score_file =open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="") #줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
score_file.close()



    #몇줄인줄 모를떄 - 반복문으로,
score_file =open("score.txt", "r", encoding="utf8")
while True:
    line =score_file.readline()
    if not line :
        break
    print(line, end="")
score_file.close()



#     # list에 넣어서 처릐!
score_file =open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #모든 라인을 가져와서, list로 저장
for line in lines:
    print(line, end="")
score_file.close()
