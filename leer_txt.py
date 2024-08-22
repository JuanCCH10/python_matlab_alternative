from tools import *

# nombre del archivo
archivo = "simbolos.txt"

# llamado de función 
array1 = leer_txt(archivo)

# conversión a lista
#lista = np.array(array1.readlines())
lista = array1
print(type(lista))

# https://astrofrog.github.io/py4sci/_static/08.%20Reading%20and%20writing%20files.html
# revisar como va tratando la información leída hasta llegar a la extracción de valores numericos

# 
nid_long = 32
block_long = 98
block_num = 3 # sin considerar el nid
for i_aux in range(0,block_num):
        block = [lista[i] for i in range(nid_long+block_long*i_aux,nid_long+block_long*(i_aux+1))]
        block = np.array(block)
        print(type(block))
        print(block)
        nombre = 'block_'+ str(i_aux+1)
        

        #block = str(block)
        #escribir_txt(nombre,block)


#count = np.arange(98)
#print(count)
#count = interleave(count)
#print(count)
#count = d_interleave(count)
#print(count)