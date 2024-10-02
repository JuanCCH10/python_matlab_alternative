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
# Valores utilizados en vivado
    # "0000", #0 est0
    # "0100", #4
    # "0001", #1
    # "0101", #5
    # "0011", #3
    # "0111", #7
    # "0010", #2
    # "0110", #6
    # "1000", #8 est1
    # "1100", #12
    # "1001", #9
    # "1101", #13
    # "1011", #11
    # "1111", #15
    # "1010", #10
    # "1110", #14
    # "0100", #4 est2
    # "0010", #2
    # "0101", #5
    # "0011", #3
    # "0111", #7
    # "0001", #1
    # "0110", #6
    # "0000", #0
    # "1100", #12 est3
    # "1010", #10
    # "1101", #13
    # "1011", #11
    # "1111", #15
    # "1001", #9
    # "1110", #14
    # "1000", #8
    # "0010", #2 est4
    # "0110", #6
    # "0011", #3
    # "0111", #7
    # "0001", #1
    # "0101", #5
    # "0000", #0
    # "0100", #4
    # "1010", #10 est5
    # "1110", #14
    # "1011", #11
    # "1111", #15
    # "1001", #9
    # "1101", #13
    # "1000", #8
    # "1100", #12
    # "0110", #6 est6
    # "0000", #0
    # "0111", #7
    # "0001", #1
    # "0101", #5
    # "0011", #3
    # "0100", #4
    # "0010", #2
    # "1110", #14 est7
    # "1000", #8
    # "1111", #15
    # "1001", #9
    # "1101", #13
    # "1011", #11
    # "1100", #12
    # "1010"]  #10

from tools import *
from trellis_viterbi import *

# leer el archivo
archivo_in = 'py_trell34_0.txt'
list_txt = leer_txt(archivo_in)
list_dat = [str(num.strip()) for num in list_txt]
# omitir el primer elemento de la lista
del list_dat[0]
# evaluación hacia adelante
aux = []
probe_dat = ['0', '0', '0', '0']



# for ik in range(len(list_dat)):
#     aux += list_dat[ik]
#     print(aux)
#     dist = hamming_dist(aux,probe_dat)
#     print('distancia: ', dist)
#     print('\n')
#     aux = []

