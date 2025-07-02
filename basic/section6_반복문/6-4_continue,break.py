# -------------------------------------------------
# SECTION 6-4 : continue, break
# -------------------------------------------------

absentKids = [2,5] #결석하면 다음 번호 진행
no_book = [7] #책은 꼭 있어야해
for student in range(1, 11) :
    if student in absentKids: 
        continue #이거 만나면 밑에거 skip
    elif student in no_book :
        print("책없으면 수업 못해. 오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 일어나서 책 읽어봐".format(student))


