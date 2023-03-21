import math

class Rocket:

    def __init__(self, Name, x = 0, y = 0):
        self.x = x
        self.y = y
        self.Name = Name

    def getPosition(self):

        """Funkcja:
            funkcja do ustalania pozycji rakiety w danym momencie
        Input:
        Output:
            currentPosition (list) - lista składająca się z kolejno współrzędnej x i y położenia rakiety na płaszczyźnie"""
        
        currentPosition = [self.x, self.y]
        return currentPosition
        
    def move(self, a, b):

        """Funkcja:
            funkcja do przesuwania rakiety o podany wektor
        Input:
            a (float) - współrzędna x wektora przesunięcia
            b (float) - współrzędna y wektora przesunięcia
        Output:
            currentPosition (list) - lista składająca się z kolejno współrzędnej x i y położenia rakiety na płaszczyźnie po przesunięciu"""
        
        self.a = a
        self.b = b
        self.x -= self.a
        self.y += self.b
        currentPosition = [self.x, self.y]
        return currentPosition
        
    def getDistance(self, rakieta):

        """Funkcja:
            funkcja do obliczania odległości między dwoma rakietami
        Input:
            rakieta (object) - objekt o zmiennych: nazwa, współrzędna x położenia na płaszczyźnie, współrzędna y położenia na płaszczyźnie
        Output:
            currentPosition (list) - lista składająca się z kolejno współrzędnej x i y położenia rakiety na płaszczyźnie po przesunięciu"""
        
        self.rakieta = rakieta
        dystans = math.sqrt((self.x - rakieta.x)**2 + (self.y - rakieta.y)**2)
        return dystans
    
    def collision(self, rakieta):           #zad 4

        """Funkcja:
            funkcja wykrywa kolizje mięzy dwoma rakietami
        Input:
            rakieta (object) - obiekt o zmiennych: nazwa, wspoółrzędna x, współrzędna y
        Output:
            True/False (bool) - gdzie True oznacza wykrycie kolizji, a False jej brak"""

        self.rakieta = rakieta
        if self.getDistance(rakieta) == 0:
            return True
        else:
            return False

    def nazwa(self):
        
        nazwa = self.Name
        return nazwa

    def __str__(self):

        return("Rakieta: " + self.Name + "  Pozycja: x = " + str(self.x) + " y = " + str(self.y))



