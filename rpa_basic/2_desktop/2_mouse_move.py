import pyautogui

# 마우스 이동
# 지정한 위치(가로x, 세로y)로 마우스 이동
# pyautogui.moveTo(300,300) # 듀얼모니터 쓸때는 좀 보긴해야함
# pyautogui.moveTo(100,100, duration=5)



# pyautogui.moveTo(100,100, duration=0.25) 
# pyautogui.moveTo(200,200, duration=0.25)
# pyautogui.moveTo(300,400, duration=0.25)

#절대 좌표로 이동 : moveTo
#상대 좌표로 이동 : move


# pyautogui.moveTo(100,100, duration=0.25) 
# print(pyautogui.position())
# pyautogui.move(100,100, duration=0.25) 
# print(pyautogui.position())
# pyautogui.move(100,100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100,100, duration=0.25)
# print(pyautogui.position()) #point(x,y)


p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)