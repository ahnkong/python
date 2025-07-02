class JapanPackage:
    def detail(self):
        print("[도쿄 패키지 4박 5일] 도쿄타워, 시부야 여행(스크램블 거리) 80만원")



if __name__ == "__main__": # 메인일때는
    print("Japan 모듈을 직접 실행")
    print("이문장은 모듈을 직접 실행할 때만 실행돼요!")
    trip_to = JapanPackage()
    trip_to.detail()


else : #11-4 모듈 직접 실행.py 에서 실행할때는, else가 실행!
    print("Japan 외부에서 모듈 호출!")   