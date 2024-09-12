from tools import *
from trellis_viterbi import *

# Pseudocódigo
# Leer archivo: in_trib0.txt
# Escribir un primer nibble cero en el archivo de salida
# Codificar según el FSM trellis 3/4
# Escribir en el archivo de salida cada uno de los datos resultantes de la codificación

# Leer el archivo
archivo = 'Datos de prueba/in_trib0.txt'
array1 = leer_txt(archivo)
list_content = [str(num.strip()) for num in array1]

# Escritura primer nibble en cero
archivo_out = 'py_trell34_0.txt'
escribir_txt(archivo_out, '0000' + '\n')

# Codificación Trellis
##Se comienza desde el estado cero
##La entrada actual es el estado siguiente
estado = '000'
for i in range(len(list_content)):
    cod_dat = trellis_34(estado,list_content[i])
    estado = list_content[i]
    escribir_txt(archivo_out,cod_dat+'\n')