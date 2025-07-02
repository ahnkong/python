print("Python", "java", "JavaScript", sep=" vs ", end="?") # 두개의 문장을 끊기지 않게 한줄로 출력해주고, 끝을 ? 로 붙여달라! 
print("무엇이 더 재미있을까요???") #end="?" 한줄로 출력됨!!!


import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)


#---------------------------------------------------
# 8-1) 표준 입출력
#---------------------------------------------------


# 오른쪽 왼쪽 정렬
# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score) #튜플로 2개를 묶어서, 출력
    print(subject.ljust(3), str(score).rjust(8), sep=":")



# 은행 대기 순번표
# 001, 002, 003, 004, 이렇게 00이 붙음
# zfill(00)
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))


answer = input("아무 값이나 입력하세용")
print(type(answer))
print("입력하신 값은 : " +  answer + " 입니다.")
# input으로 입력받은 건 다 문자열
