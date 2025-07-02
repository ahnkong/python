

# -------------------------------------------------
# SECTION 5-5 : 자료구조의 변경
# -------------------------------------------------

menu ={"커피", "우유", "주스"} #set
print(menu)
print(menu, type(menu)) #무슨 타입인지 알려줌



menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

#{'우유', '커피', '주스'} <class 'set'>
#['우유', '커피', '주스'] <class 'list'>
#('우유', '커피', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) #{'우유', '커피', '주스'} <class 'set'>



