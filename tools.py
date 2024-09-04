import numpy as np

# función para lectura de archivo
def leer_txt(file_name):
    lectura = open(file_name,"r")
    return lectura

# función para escritura de archivos
def escribir_txt(file_name,content):
    escritura = open(file_name,"a")
    escritura.write(content)
    escritura.close()

# función para desentrelazar simbolos
def d_interleave(lista):
    recover = []
    index = [0,1,8,9,16,17,24,25,32,33,40,41,48,49,56,57,64,65,72,73,80,81,88,89,96,97,2,3,10,11,18,19,26,27,34,35,42,43,50,51,58,59,66,67,74,75,82,83,90,91,4,5,12,13,20,21,28,29,36,37,44,45,52,53,60,61,68,69,76,77,84,85,92,93,6,7,14,15,22,23,30,31,38,39,46,47,54,55,62,63,70,71,78,79,86,87,94,95] 
    for i in range(len(index)):
        recover.append(lista[index[i]])
    return recover

# función para entrelazar datos en una lista
def interleave(test_list):
    index = [0,1,8,9,16,17,24,25,32,33,40,41,48,49,56,57,64,65,72,73,80,81,88,89,96,97,2,3,10,11,18,19,26,27,34,35,42,43,50,51,58,59,66,67,74,75,82,83,90,91,4,5,12,13,20,21,28,29,36,37,44,45,52,53,60,61,68,69,76,77,84,85,92,93,6,7,14,15,22,23,30,31,38,39,46,47,54,55,62,63,70,71,78,79,86,87,94,95] 
    interl = np.zeros(98)
    for i in range(0,98):
        interl[index[i]] = test_list[i]
    return interl

# función para demapear datos de una lista
# lista de prueba
#lista_mapeada = ['00','10','10','10','01','11','11','11','11','10','01','10','10','11','00','11','11','01','01','01','10','00','00','00','00','01','10','01','01','00','11','00']
def demap(mapeado):
    demapeado = ['0000'] #parte del formato para la simulación de vivado, no forma parte de la información
    for i in range(len(mapeado)):
        if i%2 :
            aux = aux + mapeado[i]
            match aux:
                case '0010':
                    demapeado.append('0000')
                case '1010':
                    demapeado.append('0001')
                case '0111':
                    demapeado.append('0010')
                case '1111':
                    demapeado.append('0011')
                case '1110':
                    demapeado.append('0100')
                case '0110':
                    demapeado.append('0101')
                case '1011':
                    demapeado.append('0110')
                case '0011':
                    demapeado.append('0111')
                case '1101':
                    demapeado.append('1000')
                case '0101':
                    demapeado.append('1001')
                case '1000':
                    demapeado.append('1010')
                case '0000':
                    demapeado.append('1011')
                case '0001':
                    demapeado.append('1100')
                case '1001':
                    demapeado.append('1101')
                case '0100':
                    demapeado.append('1110')
                case '1100':
                    demapeado.append('1111')
        else:
            aux = mapeado[i]
    return demapeado

def bin2hex(nibble_list):
    conv_list = []
    for i in range(len(nibble_list)):
        aux = nibble_list[i]
        match aux:
            case '0000':
                conv_list.append('0')
            case '0001':
                conv_list.append('1')
            case '0010':
                conv_list.append('2')
            case '0011':
                conv_list.append('3')
            case '0100':
                conv_list.append('4')
            case '0101':
                conv_list.append('5')
            case '0110':
                conv_list.append('6')
            case '0111':
                conv_list.append('7')
            case '1000':
                conv_list.append('8')
            case '1001':
                conv_list.append('9')
            case '1010':
                conv_list.append('A')
            case '1011':
                conv_list.append('B')
            case '1100':
                conv_list.append('C')
            case '1101':
                conv_list.append('D')
            case '1110':
                conv_list.append('E')
            case '1111':
                conv_list.append('F')
    return conv_list
