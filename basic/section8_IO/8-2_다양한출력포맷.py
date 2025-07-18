#---------------------------------------------------
# 8-2) 다양한 출력 포맷
#---------------------------------------------------

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일땐+ 음수일땐 -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 , 찍어주기
print("{0:,}".format(1000000000000))

# 3자리 마다 , 찍어주기 + - 부하도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))


# 3자리 마다 , 찍어주기 + - 부호도 붙이고 30자릿수도 확보
# 돈많으면 행복하니까 빈자리는 ^으로
print("{0:^<+30,}".format(1000000000000))

#소수점 출력
print("{0:.2f}".format(5/3))
