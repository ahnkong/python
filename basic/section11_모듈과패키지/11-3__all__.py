#모듈을 모아둔 집합 -> travel 폴더


# #1
# import travel.japan
# trip_to = travel.japan.JapanPackage()
# trip_to.detail()


# #2 : from   ~ import  모듈, 패키지, 클래스 다 호출 가넝
# from travel.japan import JapanPackage
# trip_to = JapanPackage()
# trip_to.detail()

#1=2 같은건데, 직접 클래스를 호출하냐, 파일을 호출하냐 그 차잉!

# import travel.barsha
# trip_to = travel.barsha.BarshaPackage()
# trip_to.detail()

# from travel import barsha
# trip_to = barsha.BarshaPackage()
# trip_to.detail()


from travel import *
trip_to = japan.JapanPackage()
# trip_to = barsha.BarshaPackage()
trip_to.detail()
