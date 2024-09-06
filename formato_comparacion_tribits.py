from tools import *

# nombre del archivo fuente
archivo = "Datos de entrada FTP/03_block_5_out.txt"
nombre = '03_block_5_out_hex.txt'

array1 = leer_txt(archivo)

lista_num = [str(num.strip()) for num in array1]

lista_num.remove('UUU')  # se remueve el primer dato que e sun defecto en la escritura de los archivos

#Estrategia, concatenar todos los valores y despues recortar en nibbles
#concatenar, omitir el pultimo valor
aux_conc = []
for i in range(len(lista_num)-1):
    aux_conc += lista_num[i]

cont = 0
aux = ''
nibble_list = []
for i in range(len(aux_conc)):
    if cont<4:
        aux = aux + aux_conc[i]
        if cont == 3:
            nibble_list.append(aux)
        cont = cont+1    
    else:
        aux = aux_conc[i]
        cont = 1

hex_list = bin2hex(nibble_list) # conversión a notación hexadecimal

for i in range(len(hex_list)):
    if i%2 :
        escribir_txt(nombre,hex_list[i]+' ')
    else:
        escribir_txt(nombre,hex_list[i])
