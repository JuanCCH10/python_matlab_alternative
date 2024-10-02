def trellis_34(estat,data):
    match estat:
        case '000':
            match data:
                case '000':
                    cod_data = '0000'
                case '001':
                    cod_data = '1000'
                case '010':
                    cod_data = '0100'
                case '011':
                    cod_data = '1100'
                case '100':
                    cod_data = '0010'
                case '101':
                    cod_data = '1010'
                case '110':
                    cod_data = '0110'
                case '111':
                    cod_data = '1110'
        case '001':
            match data:
                case '000':
                    cod_data = '0100'
                case '001':
                    cod_data = '1100'
                case '010':
                    cod_data = '0010'
                case '011':
                    cod_data = '1010'
                case '100':
                    cod_data = '0110'
                case '101':
                    cod_data = '1110'
                case '110':
                    cod_data = '0000'
                case '111':
                    cod_data = '1000'
        case '010':
            match data:
                case '000':
                    cod_data = '0001'
                case '001':
                    cod_data = '1001'
                case '010':
                    cod_data = '0101'
                case '011':
                    cod_data = '1101'
                case '100':
                    cod_data = '0011'
                case '101':
                    cod_data = '1011'
                case '110':
                    cod_data = '0111'
                case '111':
                    cod_data = '1111'
        case '011':
            match data:
                case '000':
                    cod_data = '0101'
                case '001':
                    cod_data = '1101'
                case '010':
                    cod_data = '0011'
                case '011':
                    cod_data = '1011'
                case '100':
                    cod_data = '0111'
                case '101':
                    cod_data = '1111'
                case '110':
                    cod_data = '0001'
                case '111':
                    cod_data = '1001'
        case '100':
            match data:
                case '000':
                    cod_data = '0011'
                case '001':
                    cod_data = '1011'
                case '010':
                    cod_data = '0111'
                case '011':
                    cod_data = '1111'
                case '100':
                    cod_data = '0001'
                case '101':
                    cod_data = '1001'
                case '110':
                    cod_data = '0101'
                case '111':
                    cod_data = '1101'
        case '101':
            match data:
                case '000':
                    cod_data = '0111'
                case '001':
                    cod_data = '1111'
                case '010':
                    cod_data = '0001'
                case '011':
                    cod_data = '1001'
                case '100':
                    cod_data = '0101'
                case '101':
                    cod_data = '1101'
                case '110':
                    cod_data = '0011'
                case '111':
                    cod_data = '1011'
        case '110':
            match data:
                case '000':
                    cod_data = '0010'
                case '001':
                    cod_data = '1010'
                case '010':
                    cod_data = '0110'
                case '011':
                    cod_data = '1110'
                case '100':
                    cod_data = '0000'
                case '101':
                    cod_data = '1000'
                case '110':
                    cod_data = '0100'
                case '111':
                    cod_data = '1100'
        case '111':
            match data:
                case '000':
                    cod_data = '0110'
                case '001':
                    cod_data = '1110'
                case '010':
                    cod_data = '0000'
                case '011':
                    cod_data = '1000'
                case '100':
                    cod_data = '0100'
                case '101':
                    cod_data = '1100'
                case '110':
                    cod_data = '0010'
                case '111':
                    cod_data = '1010'
    return cod_data

# distancia de hamming entre dos listas cuyos elementos son bits
def hamming_dist(dat1,dat2):
    dist = 0
    for ik in range(len(dat1)):
        if dat1[ik] != dat2[ik]:
            dist = dist + 1
    return dist

 = []

def eval 