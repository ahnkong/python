
#---------------------------------------------------
# 7-4) 가변인자
#---------------------------------------------------
    # 고정값이 아닌, 늘어남에 따라 늘어날 수 있도록

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t 나이: {1}\t".format(name, age), end=" ")
#     for lang in language :
#         print(lang, end=" ")
#     print()

# profile("아구몬", 20, "파이썬", "자바", "c", "C++", "코틀린", "javascript")
# profile("파닥몬", 20, "코틀린", "swift")