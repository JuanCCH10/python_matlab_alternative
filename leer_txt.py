from tools import *

print("inicio")

# nombre del archivo
archivo = "simbolos.txt"

# llamado de función 
array1 = leer_txt(archivo)  #no es posible imprimir la variable de manera directa, deben usarce readline() o readlines()

# conversión a lista
lista = array1.readlines()

#el archivo llega hasta la línea 424, es decir el indice 423 por inicar desde 0
nid_long = 32
block_long = 98
block_num = 3 # sin considerar el nid
for i_aux in range(0,block_num):
        block = [lista[i] for i in range(nid_long+block_long*i_aux,nid_long+block_long*(i_aux+1))]
        nombre = 'block_'+ str(i_aux+1)
        

        #block = str(block)
        #escribir_txt(nombre,block)


count = np.arange(98)
print(count)
count = interleave(count)
print(count)
count = d_interleave(count)
print(count)

print("fin")