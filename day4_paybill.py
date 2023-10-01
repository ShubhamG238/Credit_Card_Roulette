import random
ask=input("write everybody's name separated by a , \n ")
names=ask.split(",")
nn=len(names)
rn = names[random.randint(0, nn-1)]
print(rn)