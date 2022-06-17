import math as raiz
from abc import ABCMeta

class Hexagono(ABCMeta):

    @staticmethod
    def calcularPerimetro(cateto):
        cateto = cateto
        perimetro = cateto * 6
        return perimetro

    @staticmethod
    def calcularApotema(cateto):
        cateto = cateto
        apotema = (raiz.sqrt((cateto * cateto) - ((cateto / 2) * (cateto / 2))))
        apotema = round(apotema, 2)
        return apotema

    @staticmethod
    def calcularArea(perimetro, apotema):
        perimetro = perimetro
        apotema = apotema
        area = (perimetro * apotema) / 2
        area = round(area, 2)
        return area
