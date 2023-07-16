import random
number=random.randint(1,10000)
guess=int(input("DOAN SO MA TO DANG NGHI TU 1 DEN 10000"))
while guess!=number:
    if guess < number:
        print("SO BAN CHON QUA NHO...")
    else:
        print("so ban chon qua to...")
    guess=int(input("xin hay doan lai..."))
print("ban da doan dung.yayayayaya")
