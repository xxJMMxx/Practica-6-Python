from Archivos.Hexagono import Hexagono

class pruebaArchivos:

    def leerDatos(self, archivo):
        file = open(archivo, 'r')
        lineas = []
        lineas_archivo = []
        for linea in file.readlines():
            lineas.append(linea.replace('\n', '').split(";"))
        file.close()
        for f in range(0, len(lineas)):
            try:
                lineas_archivo.append([int(lineas[f][0])])
            except ValueError:
                lineas_archivo.append([0])
        return lineas_archivo

    def calcularPAA(self, lista):
        resultado = []
        for f in range(0, len(lista)):
            resultado.append([Hexagono.calcularPerimetro(
                lista[f][0]), Hexagono.calcularApotema(
                lista[f][0]), Hexagono.calcularArea(Hexagono.calcularPerimetro(
                 lista[f][0]), Hexagono.calcularApotema(
                 lista[f][0]))])
        return resultado

    def guardarResultados(self, entrada, resultados):
        file = open("Resultados.txt", 'w')
        file.write('Cateto     Perimetro        Apotema           Area\n')
        for f in range(0, len(entrada)):
            linea = str(entrada[f][0]) + '              ' + str(resultados[f][0]) + \
                    '         ' + str(resultados[f][1]) + \
                    '          ' + str(resultados[f][2]) + '\n'
            file.write(linea)
        file.close()


if __name__ == "__main__":
    prueba = pruebaArchivos()
    archivo = []
    archivo = prueba.leerDatos("Datos.txt")
    resultado = prueba.calcularPAA(archivo)
    prueba.guardarResultados(archivo, resultado)
