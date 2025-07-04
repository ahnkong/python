import pyautogui

# pyautogui.sleep(3) # 클릭하고자 하는 곳 호버 후 3초 대기
# print(pyautogui.position())  #화살표 위치 알려줌


# pyautogui.click(2478,21, duration=1) # 저 좌표 클릭


# 이 2개를 합친게 click()
# pyautogui.click()
# pyautogui.mouseDown() #드래그 할때, 저거를 사용하기도 함.
# pyautogui.mouseUp()


# pyautogui.doubleClick()
# pyautogui.click(clicks=500, duration=5) #매크로 할때, 계속 계속 누를때! 



# pyautogui.moveTo(400,400)
# pyautogui.mouseDown() #마우스 버튼 누른 상태
# pyautogui.moveTo(600, 500)
# pyautogui.mouseUp() #마우스 뗀 상태





pyautogui.sleep(3) # 클릭하고자 하는 곳 호버 후 3초 대기
# pyautogui.rightClick()
# pyautogui.middleClick()



# print(pyautogui.position())  #x=835, y=338
# pyautogui.moveTo(x=1181,y=602)
# pyautogui.drag(200,200,) #현재 위치 기준으로, x는 200만큼, y도 200만큼 드래그
# pyautogui.drag(835,338, duration=0.5) #너무 빠른 동작으로 drag수행 안될때는 duration 걸기!


# pyautogui.dragTo(1514,349, duration=0.25)


pyautogui.scroll(300) # 양수이면 위 방향으로 300만큼 스크롤. 음수면, -300 아래 방향으로  스크롤
