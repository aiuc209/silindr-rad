import math

def hisobla(radiuslar, balandliklar):
    yuzalar = []
    for r, h in zip(radiuslar, balandliklar):
        yuzasi = 2 * math.pi * r * h
        yuzalar.append(yuzasi)
    return yuzalar

radiuslar = [5, 10, 15]
balandliklar = [10, 20, 30]
print(hisobla(radiuslar, balandliklar))
