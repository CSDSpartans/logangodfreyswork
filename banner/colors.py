"""Colors Module

lol, rainbowz
"""

R=r=red           ="\033[0;31m"
O=o=orange        ="\033[1;31m"
Y=y=yellow        ="\033[0;33m"
G=g=green         ="\033[0;32m"
C=c=cyan          ="\033[0;36m"
B=b=blue          ="\033[0;34m"
V=v=violet        ="\033[0;35m"
M=m=magenta       ="\033[1;35m"
B03=b03=base03    ="\033[0;30m"
B02=b02=base02    ="\033[1;30m"
B01=b01=base01    ="\033[1;32m"
B00=b00=base00    ="\033[1;33m"
B0=b0=base0       ="\033[1;34m"
B1=b1=base1       ="\033[1;36m"
B2=b2=base2       ="\033[0;37m"
B3=b3=base3       ="\033[1;37m"
X=x=reset         ="\033[0m"
CL=cl=clear       ="\033[H\033[2J"

colors=[yellow,orange,red,magenta,violet,blue,cyan,green]

import random
def random_color():
    return random.choice(colors)
def rc():
    return random.choice(colors)
if __name__=="__main__":
    print(r+'Red')
    print(o+'Orange')
    print(y+'Yellow')
    print(g+'Green')
    print(c+'Cyan')
    print(b+'Blue')
    print(v+'Violet')
    print(m+'Magenta')
    print(b03+'Base03')
    print(b02+'Base02')
    print(b01+'Base01')
    print(b00+'Base00')
    print(b0+'Base0')
    print(b1+'Base1')
    print(b2+'Base2')
    print(b3+'Base3')
    input()
    print(clear)
    for count in range(111):
        color1=random_color()
        color2=random_color()
        color3=random_color()
        print(color1+'lel '+color2+'sweg '+color3+'XD ',end='')
    print(reset)

