import os
os.system('cls')
def MyBanner():
    line01 = "*" * 20
    line02 = "*" + " " * 18 + "*"
    line03 = "*    JMK Code      *"
    print("")
    print(line01)
    print(line02)
    print(line03)
    print(line02)
    print(line01)
    print("")

MyBanner()
sentence = "I'm back at work"
print(sentence)
print("")

title = "MENU"  # "Menu".upper() is directly "MENU"
print(title)
print(title.center(40, "-"))
MyBanner()
print(sentence[4])