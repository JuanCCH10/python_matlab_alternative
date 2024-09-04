from tools import *

# nombre del archivo fuente
archivo = "Datos de entrada FTP/03_block_1_out.txt"
nombre = '03_block_1_out_hex.txt'

array1 = leer_txt(archivo)

lista_num = [str(num.strip()) for num in array1]

lista_num.remove('UU')  # se remueve el primer dato que e sun defecto en la escritura de los archivos

nibble_list = []        # se agrupan los datos en nibbles previo a la conversión bin2hex
for i in range(len(lista_num)):
    if i%2 :
        aux = aux + lista_num[i]
        nibble_list.append(aux)
    else:
        aux = lista_num[i]

hex_list = bin2hex(nibble_list) # conversión a notación hexadecimal

for i in range(len(hex_list)):
    escribir_txt(nombre,hex_list[i])
