# anggota = ("riyadi", 20, True, 3.96, ["APD", 25], ("samarinda", 12))

# print(anggota[4][0])

# list awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
liststudy = list(studyclub)
# tuple awal
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# Ubah tuple menjadi list
liststudy = list(studyclub)
# Tambahkan Web
liststudy.append("Web")
# ubah kembali list menjadi tuple
studyclub = tuple(liststudy)
print(studyclub)
