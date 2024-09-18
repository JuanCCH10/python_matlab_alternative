from tools import *

# nombre del archivo fuente
archivo_in = 'Datos a procesar/MSN_D_Confirm.txt'
archivo_out = 'MSN_D_Confirm_out.txt'
array1 = leer_txt(archivo_in)
list_content = [str(num.strip()) for num in array1]

aux_conc = []
for i in range(len(list_content)):
    aux_conc += list_content[i]

print('# bits :', len(aux_conc))

# son 144 bits por linea
# serían 36 nibbles
# es decir 18 bytes

aux = ''
cont = 0
nibble_list = []
for i in range(len(aux_conc)):
    if cont < 4:
        aux = aux + aux_conc[i]
        if cont == 3:
            nibble_list.append(aux)
        cont = cont + 1
    else:
        aux = aux_conc[i]
        cont = 1

print('# nibbles :', len(nibble_list))

hex_list = bin2hex(nibble_list)

print('# hex :', len(hex_list))

cont = 0
byte_list =[]
aux = ''
for i in range(len(hex_list)):
    if i%2 :
        aux = aux + hex_list[i] + ' '
        byte_list.append(aux)
    else:
        aux = hex_list[i]

print('# byte :',len(byte_list))

cont = 1
for i in range(len(byte_list)):
    if cont == 18:
        escribir_txt(archivo_out,byte_list[i]+'\n')
        # print(byte_list[i] + '\n')
        cont = 1
    else:
        escribir_txt(archivo_out,byte_list[i])
        # print(byte_list[i])
        cont = cont + 1