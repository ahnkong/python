# #1. glob: 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# import glob
# print(glob.glob("*.py"))



# 2. os : 운영체제에서 제공하는 기본 기능 ( 폴더 조회, 삭제 등등)
import os
# print(os.getcwd()) #현재 디렉토리

# folder ="sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다!")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니당!")
# else :
#     os.makedirs(folder) #폴더 생성
#     print(folder,"폴더를 생성하였습니다!")


# print(os.listdir()) #경로

# # 3. time : 시간관련 함수
# import time
# print(time.localtime()) 
# print(time.strftime("%Y-%m-%d %H:%M:%S")) #오늘 날짜는  2025-07-02


import datetime
# print("오늘 날짜는 ", datetime.date.today()) #오늘 날짜는  2025-07-02


# timedelta : 두 날짜 사이의 간격
today =datetime.date.today()            #오늘 날짜
td = datetime.timedelta(days=100)       #100일저장
print("우리가 만난지 100일은", today+td) #오늘부터 100일 후