
import random as rd
lisT = []
for i in range(30):
    num = rd.randint(1, 30)
    lisT.append(num)
    if num > 30:
        print(f"el numero {num} es alto")
    elif 10 < num < 20:
        print(f"el numero {num} es medio")
    else:
        print(f"el numero {num} es  bajo")
print(lisT)