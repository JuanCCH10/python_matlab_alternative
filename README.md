Algoritmo codificación Trellis 3/4
Algoritmo decodificación Viterbi 3/4

-Codificador: codificador_trellis_34.py
    °Tomar como base el formato de archivo con el que se alimenta el proyecto de vivado
        >in_trib0.txt
        48 datos de 3 bits + 1 dato de 3 bits en cero
    °Tomar como base el formato de archivo entregado por vivado posterior a la codificación
        >out_trell34_0.txt
        datos de longitud nibble, primer dato en cero no forma parte del resultado, 49 datos resultado de la codificación
-Decodificador: decodificador_viterbi_34.py