e1 = Employee(1111, "홍길동", 1000000, ["여행", "낚시", "운동"])
e1.display()
'''
사번 : 1111
이름 : 홍길동
급여 : 1000000
취미 : 여행, 낚시, 운동
'''
e2 = Employee(1112, "임꺽정", 2000000, ["여행", "자전거", "운동"])
e3 = Employee(1113, "신돌석", 3000000, ["독서", "낚시", "수영"])
total = e1.getCount()
print("총인원수 : ", total) #3

e3.setSalary(2500000)
e3.appendHobby(["피아노", "드론"])
e3.display()
'''
사번 : 1112
이름 : 신돌석
급여 : 2500000
취미 : 독서, 낚시, 수영, 피아노, 드론
'''
