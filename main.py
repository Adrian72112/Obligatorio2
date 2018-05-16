

FILA_CONTADOR = 7
COLUMNAS_CONT = 7  
width = 20
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Juego():
    
    def __init__(self,numero_filas,numero_columnas):
        self.numero_filas = numero_filas
        self.numero_columnas = numero_columnas

    def __repr__(self):
        print("BIENVENIDOS AL JUEGO 4 EN LÍNEA")
    
    def imprimir_tabla(self,tabla):  
        tablaInvert = tabla[::-1]
        print("\n".join(["".join(["{:4}".format(item) for item in fila]).center(width) for fila in tablaInvert]))

    def crear_tabla(self):
        # Crear matriz 
        tabla = []
        for i in range(self.numero_filas):
            tabla.append([])
            for j in range(self.numero_columnas):
                tabla[i].append(0)
        return tabla

    def tirar_ficha(self,tabla, fila, col, pieza):
        tabla[fila][col] = pieza

    def validar_posicion(self,tabla, col):
        return tabla[FILA_CONTADOR-1][col] == 0

    def obtener_proxima_fila(self,tabla, col):
        for r in range(FILA_CONTADOR):
            if tabla[r][col] == 0:
                return r

    def movimiento_ganador(self,tabla, pieza):
        # Chekear horizontales lugares para ganar
        for c in range(COLUMNAS_CONT-3):
            for r in range(FILA_CONTADOR):
                if tabla[r][c] == pieza and tabla[r][c+1] == pieza and tabla[r][c+2] == pieza and tabla[r][c+3] == pieza:
                    return True
        # Checkear posibles lugares verticales
        for c in range(COLUMNAS_CONT):
            for r in range(FILA_CONTADOR-3):
                if tabla[r][c] == pieza and tabla[r+1][c] == pieza and tabla[r+2][c] == pieza and tabla[r+3][c] == pieza:
                    return True

        # Checkear diagonales positivas
        for c in range(COLUMNAS_CONT-3):
            for r in range(FILA_CONTADOR-3):
                if tabla[r][c] == pieza and tabla[r+1][c+1] == pieza and tabla[r+2][c+2] == pieza and tabla[r+3][c+3] == pieza:
                    return True

        # Checkear diagonales negativos
        for c in range(COLUMNAS_CONT-3):
            for r in range(3, FILA_CONTADOR):
                if tabla[r][c] == pieza and tabla[r-1][c+1] == pieza and tabla[r-2][c+2] == pieza and tabla[r-3][c+3] == pieza:
                    return True


print(bcolors.HEADER, "BIENVENIDOS AL JUEGO 4 EN LÍNEA".center(width),bcolors.ENDC)
juego = Juego(7,7)
print("  ")
print("  ")
print("  ")

tabla = juego.crear_tabla()
juego.imprimir_tabla(tabla)
fin_juego = False
turno = 0

while not fin_juego:
    # Jugador 1 Input
    if turno == 0:
        print(" ")
        print(" ")
        print(bcolors.OKBLUE , "TURNO JUGADOR 1".center(width) ,bcolors.ENDC)
        print("---------------------".center(width))
        col = int(input("Ingrese columna a colocar (0-6): ".center(width)))
        if juego.validar_posicion(tabla, col):
            fila = juego.obtener_proxima_fila(tabla, col)
            juego.tirar_ficha(tabla, fila, col, "   X")
            if juego.movimiento_ganador(tabla,"   X"):
                print("Jugador 1 gano!!".center(width))
                fin_juego = True
                break;
    else: # Jugador 2 Input
        print(" ")
        print(" ")
        print(bcolors.OKGREEN,"TURNO JUGADOR 2 :".center(width) )
        print("---------------------".center(width))               
        col = int(input("Ingrese columna a colocar (0-6): ".center(width)))

        if juego.validar_posicion(tabla, col):
            fila = juego.obtener_proxima_fila(tabla, col)
            juego.tirar_ficha(tabla, fila, col, "   O")

            if juego.movimiento_ganador(tabla, "   O"):
                print("Jugador 2 gano!!".center(width))
                fin_juego = True
                break;

    print(bcolors.HEADER, "BIENVENIDOS AL JUEGO 4 EN LÍNEA".center(width),bcolors.ENDC)
    print("  ")
    print("  ")
    print("  ")
    print(" ")
    juego.imprimir_tabla(tabla)
    turno += 1
    turno = turno % 2


  
