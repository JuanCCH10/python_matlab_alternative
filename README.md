Para decodificar Viterbi 3/4
-Es necesario comprobar el funcionamiento de trellis-viterbi 3/4 de manera local
    °generar proyecto trellis_34_local.
        >alimentar con ...tribits.txt
        >obtener ...out.txt
    °generar proyecto viterbi_34_local
        >alimentar con ...out.txt
        >recuperar ...tribits.txt
Para la comprobación será necesario revisar los archivos de simulación y verificar que 
trellis sea sin mapeador.
-Una vez verificado lo anterior, se deberá alimentar viterbi_34_local con los bloques 
segmentados: 0x_block_x.txt. Se generarán los archivos: 0x_block_x_out.txt
Dichos archivos deberán llevarse a su formato final en hex mediante 
formato_comparacion.py, generando los archivos: 0x_block_x_out_hex.txt

-Se creó el proyecto trellis_34_local
    °no tiene mapeador
    °archivo de entrada: in_trib0.txt
    °archivo de salida: out_trell34_0.txt
        >agrega un cero al final que forma parte de la codificación
-Se creo el proyecto viterbi_34_local
    °Se tomo como referncia el nombre del archivo en virgula_v1, se trata de ...V3.
        >Se empleo el archivo local
    °archivo de entrada: out_trell34_0.txt
    °archivo de salida: recover_trib0.txt
-Se generó verificación_trellis-viterbi_local.py para comparación de los archivos.
    °in_trib0.txt
    °recover_trib0.txt
    °Verificación exitosa
-Decodificación de bloques faltantes
    °archivos de entrada: 0x_block_x.txt, los bloques que no son 1
    °archivos de salida: 0x_block_x_out.txt
-Formato para comparación
    °Se generó el archivo: formato_comparacion_tribits.py
        >archivo de entrada: 0X_block_X_out.txt
        >archivo de esalida: 0X_block_X_out_hex.txt
