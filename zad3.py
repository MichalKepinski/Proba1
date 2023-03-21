import rocket as r
import płaszczyzna as p
import random

rakieta1 = r.Rocket("rakieta1")
rakieta2 = r.Rocket("rakieta2")
rakieta3 = r.Rocket("rakieta3")
rakieta4 = r.Rocket("rakieta4")
rakieta5 = r.Rocket("rakieta5")

rakiety = [rakieta1, rakieta2, rakieta3, rakieta4, rakieta5]

for i in range(4):
    rakieta1.move(random.uniform(-10,10), random.uniform(-10,10))
    rakieta2.move(random.uniform(-10,10), random.uniform(-10,10))
    rakieta3.move(random.uniform(-10,10), random.uniform(-10,10))
    rakieta4.move(random.uniform(-10,10), random.uniform(-10,10))
    rakieta5.move(random.uniform(-10,10), random.uniform(-10,10))
    p.rysunek(rakiety)

for i in range(len(rakiety)):
    print(rakiety[i])

for el in rakiety:                              #zrobić żeby pary sie nie powtarzały??
    for elem in rakiety:
        if el != elem:
            print("dystans między", el.nazwa(), "i", elem.nazwa(), "to", el.getDistance(elem))
