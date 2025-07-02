

# -------------------------------------------------
# SECTION 5-4 : 세트(집합)
#  중복안됨. 순서 없음
# -------------------------------------------------
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)

print(java.intersection(python))


#합집합 (java와 python을 할 수 있는 모든 개발자)
print(java | python)
print(java.union(python))


#차집합 (java는 할 수 있지만, python을 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))


# 파이썬 할 줄 아는 사람이 늘어남
python.add("지예은")
print(python)


# 김태호 java 안한지 오래돼서 까묵음
java.remove("김태호")
print(java)
