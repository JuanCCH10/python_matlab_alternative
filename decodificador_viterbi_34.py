# Lectura de datos:
#   °Leer py_trell34_0.txt
#       -Omitir el primer dato, es un cero
#   °Evaluación hacia enfrente
#       -Cada dato a continuación debe ser evaluado mediante el diagrama de trellis
#           >La evaluación del diagrama de trellis requiere evaluar el número de bits 
#           diferentes entre el dato actual y el valor asociado a la rama del
#           diagrama. 
#           >La evaluación anterior nos lleva a la generación de un peso por rama
#           y un peso por estado. El peso por rama es el resultado directo de la 
#           evaluación de bits diferentes (distancia de Hamming), mientras que 
#           el peso por estado corresponde a la suma del peso acumulado y el peso
#           de rama
#   °Decisión hacia atrás
#       -Se trata de la elección de la ruta de menor peso. Cuando la información no
#       no posee errores la ruta se caracteríza por ser la de peso igual a cero en 
#       todas sus transiciones.
#           >La decisión hacia atrás depende de la información almacenada durante
#           la evaluación hacia adelante. 

from tools import *

# leer el archivo
archivo_in = 'py_trell34_0.txt'
list_txt = leer_txt(archivo_in)
list_dat = [str(num.strip()) for num in list_txt]
print(list_dat)
# omitir el primer elemento de la lista
del list_dat[0]
print(list_dat)
# evaluación hacia adelante
aux = []
for i in range(len(list_dat)):
    aux += list_dat[i]
    print(aux)
    del aux