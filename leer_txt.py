# función para lectura de archivo
def leer_txt(file_name):
    lectura = open(file_name,"r")
    return lectura

# función para escritura de archivos
def escribir_txt(file_name,content):
    escritura = open(file_name,"w")
    escritura.write(content)
    escritura.close()

# función para desentrelazar simbolos
def d_interleave(lista)
    interl_index = [0,1,8,9,16,17,24,25,32,33,40,41,48,49,56,57,64,65,72,73,80,81,88,89,96,97,2,3,10,11,18,19,26,27,34,35,42,43,50,51,58,59,66,67,74,75,82,83,90,91,4,5,12,13,20,21,28,29,36,37,44,45,52,53,60,61,68,69,76,77,84,85,92,93,6,7,14,15,22,23,30,31,38,39,46,47,54,55,62,63,70,71,78,79,86,87,94,95]
    d_list = [lista[i] for i in interl_index]
    print(d_list)

print("inicio")

# nombre del archivo
archivo = "simbolos.txt"

# llamado de función 
array1 = leer_txt(archivo)  #no es posible imprimir la variable de manera directa, deben usarce readline() o readlines()

# conversión a lista
lista = array1.readlines()

# calculo de indices
#indices de nid n/a:     0->31
#indices de header 1/2:  32->(32+98)-1 = A
#indices de b1 3/4:      A+1->(A+98) = B
#indices de b2 3/4:      B+1->(B+98) = C
#indices de b3 3/4:      C+1->(C+98)
#el archivo llega hasta la línea 424, es decir el indice 423 por inicar desde 0
nid_long = 32
block_long = 98
block_num = 3 # sin considerar el nid
for i_aux in range(0,block_num):
        block = [lista[i] for i in range(nid_long+block_long*i_aux,nid_long+block_long*(i_aux+1))]
        nombre = 'block_'+ str(i_aux+1)
        

        #block = str(block)
        #escribir_txt(nombre,block)

print("fin")
