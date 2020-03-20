import sqlalchemy as db
import pyodbc
import re
import os

class QueenChessBoard:
    def __init__(self, size):
        
        self.size = size
        self.columnas = []
        self.posicionesReina=[]
        self.solTot=[]
 
    def setReina(self, column):
        self.columnas.append(column)
 
    def extractReina(self):
        return self.columnas.pop()
 
    def Validacion(self, column):
       
        row = len(self.columnas)
 
        for i in self.columnas:
            if column == i:
                return False
 
        for j, i in enumerate(self.columnas):
            if i - j == column - row:
                return False
        for j, i in enumerate(self.columnas):
            if ((self.size - i) - j
                == (self.size - column) - row):
                return False
 
        return True
 
    def show_Board(self):
        print(end='  ')
        for w in range(self.size):
            print(w,end=' ')
        print()
        for row in range(self.size):
            print(row,end=' ')
            for column in range(self.size):
                if column == self.columnas[row]:
                    print('i', end=' ')
                    self.posicionesReina.append([column,row])
                else:
                    print('*', end=' ')
            print()
        print("Posiciones resultantes: ",self.posicionesReina)
        self.solTot.append(self.posicionesReina)
        self.posicionesReina=[]
 
 
def solve_Reinas(size):
    Conection()
    tablero = QueenChessBoard(size)
    sol = 0
 
    row = 0
    column = 0
    
    while True:
       
        while column < size:
            if tablero.Validacion(column):
                tablero.setReina(column)
                row += 1
                column = 0
                break
            else:
                column += 1
 
        
        if (column == size or row == size):
            
            if row == size:
                tablero.show_Board()
                print()
                sol += 1
 
               
                tablero.extractReina()
                row -= 1
 
            try:
                prev_column = tablero.extractReina()
            except IndexError:
                
                break
            
            row -= 1
            column = 1 + prev_column
 
    print('Soluciones encontradas :', sol)

def Conection():
    try:
        engine = db.create_engine('mssql+pyodbc://DESKTOP-GFR7BPN\SANDRA:12345@DESKTOP-GFR7BPN\TEW_SQLEXPRESS:tew_app_data/dbO.Hoja1$').connect()
        print("Conexión exitosa con la base de datos.")
    except:
        print("Hubo un error en la dirección de la base de datos. :(")

repeat=True
while(repeat==True):
    n = int(input('Dimensión del tablero: '))
    solve_Reinas(n)
    print('Desea buscar otras Soluciones para otro tablero? ')
    answ=str(input())
    if(re.match('([Ss][íÍ]|[Yy][eE][Ss]|[oO][Uu][Ii]|[Jj][aA]|[Ss]|[Yy])+(\s|,).',answ)):
        os.system("Cls")
        repeat=True
    else:
        print('Finalizando la ejecución')
        repeat=False
