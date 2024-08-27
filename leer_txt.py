from tools import *

# nombre del archivo fuente
archivo = "Datos de entrada FTP/03_MSN_D_Confirm.txt"
# nomenclatura de los archivos resultado
file_gen_name = '03_block_'
block_num = 5 # sin considerar el nid

array1 = leer_txt(archivo)

lista_num = [str(num.strip()) for num in array1] # asignar el contenido del archivo a una lista

nid_long = 32
block_long = 98

for i_aux in range(0,block_num):
        block = [lista_num[i] for i in range(nid_long+block_long*i_aux,nid_long+block_long*(i_aux+1))]   #recorte de bloques
        nombre = file_gen_name + str(i_aux+1) + '.txt'                                                         #nombre del archivo
        block_din = d_interleave(block)
        block_dem = demap(block_din)
        for i in range(len(block_dem)):
                escribir_txt(nombre,block_dem[i]+'\n')
