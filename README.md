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
