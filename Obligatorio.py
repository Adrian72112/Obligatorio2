class Juego():
    def  __init__(self,columna=7,fila=6):
        self.columna=columna-1
        self.fila=fila-1
    def crear_tablero(self):
        tablero=[]
        for e in range(self.fila+1):
            tablero.append([])
            for i in range(self.columna+1):
                tablero[e].append(" ")
        return tablero
    def imprimir_tablero(self,tablero):
        for e in tablero:
            print ("|"+"|".join(e)+"|")
    def lanzar_ficha(self,lugarcolumna,jugador,tablero):
        lugarcolumna=lugarcolumna-1
        k=5
        while tablero[k][lugarcolumna]!=" " and k>=0:
            k-=1
        if k<=-1:
            return print("Columna Llena")
        else:
            tablero[k][lugarcolumna]=jugador
            self.imprimir_tablero(tablero)
            return tablero

    def es_ganador(self,tablero):
    #Vertical
        for e in range(self.columna):
            for i in range(self.fila):
                
                count+=tablero[e][i]

            
            


        

juego=Juego()
tablero=juego.crear_tablero()
juego.lanzar_ficha(3,"x",tablero)



