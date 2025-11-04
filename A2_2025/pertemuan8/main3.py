import random

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""


for i in range(12):
    password = random.choice(karakter)
    kata_sandi+= password

print(kata_sandi)

    
    
