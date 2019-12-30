import os
from pathlib import Path
import sys

#RUTA DONDE SE CREARAN LAS CARPETAS
ruta = input("Ingrese nombre de carpeta a crear o ruta (c:\carpetas) : ")
print("Ruta seleccionada: ",os.getcwd(),'\\',ruta)

#Se pueden usar dos metodos para el listado de carpetas.
#La otra es una variable con una lista y la otra es leyendo un archivo que tenga nombres, separandolos con "," o espacio.
metodo = input("(1) Metodo listado\n(2) Metodo con archivo de texto \n")

#METODO LISTADO
if metodo == "1":
    print("METODO LISTADO SELECCIONADO")
   
    listado = input("Ingrese nombre de carpetas, separados por coma: \n")
    carpetas = listado.split(",")
    
#METODO ARCHIVO DE TEXTO
elif metodo == "2":
    l = input("METODO ARCHIVO DE TEXTO SELECCIONADO\nIngrese nombre listado o ruta donde se encuentra: \n")
    c = open(l)
    carpetas = (input('Listado separado por coma (,) o salto de linea (s)'))
    
    #Si el texto tiene separación por comas u otro caracter
    if carpetas == ",":
       carpetas = c.read().split('-')
       
    #Si el texto tiene salto de linea
    elif carpetas == "s":
        carpetas = [line.rstrip('\n') for line in c]
        
print("Las siguientes carpetas seran creadas: \n",carpetas,"\nEsta seguro que desea crearlas?")


while True:
    confirm = input(" s/n: ")
    if confirm == "s":
        break
    if confirm == "n":
        print("Usted cancelo la creacion")
        sys.exit()
    else:
        print("Ingrese un valor valido (s/n) ")
        continue
            
#CREACION DE CARPETAS
lc = carpetas
for carpeta in lc:
    os.makedirs(os.path.join(ruta,str(carpeta)), exist_ok=True)

#MOSTRAR CARPETAS CREADAS
for ruta, dirs, files in os.walk(ruta):
    print(os.getcwd().replace(' ',''),'\\'+ruta)
    #print (ruta)
    for f in files:
        print (f)
        
input("Carpetas creadas !!\nPresiona una tecla para finalizar.")
sys.exit()