import rocket as r
import matplotlib.pyplot as plt


def rysunek(rakiety):
    
    x = [] #współrzędne x każdej z rakiet
    y = []#analogicznie

    for i in range(len(rakiety)):
        x.append(rakiety[i].getPosition()[0])
        y.append(rakiety[i].getPosition()[1])

    plt.scatter(x, y)
    plt.title("Rakiety na płaszczyźnie")
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.show()


