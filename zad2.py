import rocket as r
import random
import płaszczyzna as p

rakieta = r.Rocket("rakieta1")
rakiety = [rakieta]

xlist = []
ylist = []

for i in range(5):
    xlist.append(random.uniform(-10, 10))
    ylist.append(random.uniform(-10, 10))

for i in range(5):
    rakieta.move(xlist[i], ylist[i])
    p.rysunek(rakiety)
    print(rakieta)



