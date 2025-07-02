# # 방법1
# import theater_module
# theater_module.price(3) #3명이서 영화 보러 갔을때의 가격
# theater_module.price_morning(4) #조조할인 영화 4명
# theater_module.price_soldier(5) #5명의 군인 영화보러 갔을때,



# #방법2
# import theater_module as mv #mv로 짧게 호출하긔
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# # 방법3
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)


# # 방법4 => 원하는 것만 쓸래여
# from theater_module import price, price_morning #군인은 안해
# price(5)
# price_morning(10)




# 방법5 => 군인만
from theater_module import price_soldier as price
price(5)