from tools import *

file1 = 'in_trib0.txt'
file2 = 'recover_trib0.txt'

info1 = leer_txt(file1)
info2 = leer_txt(file2)

list1 = [str(num.strip()) for num in info1]
list2 = [str(num.strip()) for num in info2]

list2.remove('UUU')  # se remueve el primer dato que es un encabezado de escritura

aciertos = 0
errores = 0
indices_error = []
for i in range(len(list1)):
    if list1[i] == list2[i]:
        aciertos = aciertos + 1
    else:
        errores = errores + 1
        indices_error.append(i)

print('# de datos comparados',len(list1))
if errores == 0:
    print('________________DATOS IGUALES________________')
else:
    print('# de errores: ', errores)
    print('indices de error: ',indices_error)