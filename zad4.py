import rocket as r
import płaszczyzna as p

rakieta1 = r.Rocket("rakieta1")
rakieta2 = r.Rocket("rakieta2")

rakiety = [rakieta1, rakieta2]

p.rysunek(rakiety)
print(rakieta1.collision(rakieta2))

rakieta1.move(0, 10)
rakieta2.move(-10, 0)

p.rysunek(rakiety)
print(rakieta1.collision(rakieta2))

rakieta1.move(-10, 0)
rakieta2.move(0, 10)

p.rysunek(rakiety)
print(rakieta1.collision(rakieta2))
