datos_extra_dibsout.txt
Son los datos de salida de trellis 1/2, utilizado en virgula_v1. Este trellis posee mapeador.

Para utlizar este archivo es necesario demapear y agregar un cero en la primera posición como
parte de l formato de simulación, no es parte de la información.
El archivo sería util para poder leerlo desde viterbi 1/2 local y obtener la información
original. Especial atención en la longitud recuperada, se está recuperando un cero al final
y el archivo recuperado cuenta con un UU al inicio que debe ser eliminado para utilizarlo
en la simulación de trellis.

Los datos originales se habrán de utilizar para alimentar el trellis 1/2 local y comprobar
el funcionamiento del demapeador en sw.

Secuencia de archivos:
datos_extra_dibsout.txt     -> demapeo_dibsout.py       -> dibsout_demap.txt ...
dibsout_demap.txt           -> vivado: viterbi_12_local -> recover_dibsout_demap.txt ...
recover_dibsout_demap.txt   -> vivado: trellis_12_local -> out_trell12_local.txt

out_trell12_local.txt se debe comparar contra dibsout_demap.txt
Se generó la función en tools.py para comparar achivos txt.
La función comprueba que los datos son iguales.
El problema puede ser en el desentrelazador.

Comprobación desentrelazador
Se usará el excel con el que Fermin había estado trabajando para trellis 1/2,
Este archivo desentrelaza y demapea. Nuestro punto de comparación será 01_block_1.txt
el cual podría decodificarse con el excel.

Efectivamente el problema era en los índices del desentrelazador, se tomó como referencia
el archivo de excel Entrelazador en el fichero: 
D:\GoogleDrive\Otros ordenadores\Mi PC\Mi unidad\Codigos de correccion de errores

Se puede segmentar la información con: Procesamiento datos de simulacion.py
Faltaría dar formato a la información obtenida desde viterbi_12_local y quitar el 
cero agregado al final que forma parte de la codificación

