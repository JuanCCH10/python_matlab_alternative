from tools import *

# nombre del archivo fuente
archivo = "datos_extra_dibsout.txt"
# nombre del archivo destino
destino = 'dibsout_demap.txt'
# lectura del archivo
array1 = leer_txt(archivo)
# cambio a lista
dat_map = [str(num.strip()) for num in array1]
# demapeo de nibbles
demapeo = demap_nibble(dat_map)
# escritura de archivo
for i in range(len(demapeo)):
    escribir_txt(destino,demapeo[i]+'\n')