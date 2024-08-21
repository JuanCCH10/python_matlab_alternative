# funcion para lectura de archivo
def leer_txt(file_name):
    lectura = open(file_name,"r")
    return lectura

# funcion para escritura de archivos
def escribir_txt(file_name,content):
    escritura = open(file_name,"w")
    escritura.write(content)
    escritura.close()

print("inicio")

# nombre del archivo
archivo = "simbolos.txt"

# llamado de función 
array1 = leer_txt(archivo)  #no es posible imprimir la variable de manera directa, deben usarce readline() o readlines()

# tipo de variable
print(type(array1))

# cambio de tipo mediante contructores
#array_str = str(array1)
#print(type(array_str))      #esta conversión es erronea
#los contructores int / float no aceptan tipos que no sean: str, byte o real_num

# conversión a lista
lista = array1.readlines()

# mostrar el arreglo en este punto
for i in range(0,3):
    print(lista[i])
#es posible asignar uno a uno los valores

# calculo de indices
#indices de nid n/a:     0->31
#indices de header 1/2:  32->(32+98)-1 = A
#indices de b1 3/4:      A+1->(A+98) = B
#indices de b2 3/4:      B+1->(B+98) = C
#indices de b3 3/4:      C+1->(C+98)
#el archivo llega hasta la línea 424, es decir el indice 423 por inicar desde 0
#primer intento con indices a mano
nid_long = 32
block_long = 98
nid_block = [lista[i] for i in range(0,nid_long)]
#longitud de la lista resultante
print(len(nid_block))
print(nid_block)
block1 = [lista[i] for i in range(nid_long, nid_long+block_long)]
print(len(block1))
print(block1)
block2 = [lista[i] for i in range(nid_long+block_long, nid_long+block_long*2)]
print(block2)
print(len(block2))
block3 = [lista[i] for i in range(nid_long+block_long*2, nid_long+block_long*3)]


# simplificar el código 
block_num = 3 # sin considerar el nid
for i_aux in range(0,block_num):
        block = [lista[i] for i in range(nid_long+block_long*i,nid_long+block_long*(i+1))]
        nombre = ["block_"+ str(i+1)]
        nombre = str(nombre)
        block = str(block)
        escribir_txt(nombre,block)

print("fin")
