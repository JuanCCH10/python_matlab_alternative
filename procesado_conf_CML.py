# Archivo origen: multiples caracteres en una sola línea
# Archivo destino: notación hex byte Vivado, líneas de 64 bytes
# A) Leer los datos
# B) Agruparlos en dos caracteres a la vez
#   Agregar notacion x"--"
#   Primer dato y datos a continuación: x"--",
#   Ultimo dato: x"--"

from tools import *

# A)
archivo_in = 'Datos a procesar/Conf_CML.txt'
archivo_out = 'conf_cml_out.txt'
array1 = leer_txt(archivo_in)
list_content = [str(num.strip()) for num in array1]
aux = []                # empty list
aux += list_content[0]  # esta linea ya separa los caracteres uno a uno

# B)
long_line = 64          # bytes
cont_char = 0
cont_elem = 0
for i in range(len(aux)):
    if cont_char == 0:
        byte_aux = aux[i]
        cont_char += 1
    else:
        byte_aux = byte_aux + aux[i]
        cont_char = 0
        if i == len(aux)-1:
            #byte_aux = 'x"' + byte_aux + '"'
            byte_aux = f'x"{byte_aux}"'
        else:
            #byte_aux = 'x"' + byte_aux + '",'
            byte_aux = f'x"{byte_aux}",'
        if cont_elem == 0:
            byte_list = byte_aux
        else:
            byte_list = byte_list + byte_aux 
        cont_elem += 1
        if cont_elem > long_line-1:
            print(byte_list)
            escribir_txt(archivo_out,byte_list+'\n')
            cont_elem = 0