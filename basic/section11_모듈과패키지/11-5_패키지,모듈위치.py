from travel import *
trip_to = japan.JapanPackage()
# trip_to = barsha.BarshaPackage()
trip_to.detail()

import inspect
import random

# 모듈 위치 찾아오기
print(inspect.getfile(random)) # c:\Users\USER\AppData\Local\Programs\Python\Python313\Lib\random.py 여기서 가져옴
print(inspect.getfile(japan))


