import random

listNames = ["Gifty", "Angela", "Joe", "Mclean"]
print(listNames)
totlname = len(listNames)
randomchoice = random.choice(listNames)

#print(randomchoice)

RandomName = random.randint(1, totlname)

print(listNames[RandomName])