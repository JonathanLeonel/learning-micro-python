# abro un archivo de nombre "data.txt" en modo escritura
f = open('data.txt', 'w')

# escribo en el archivo la leyenda
f.write('Hello world from python!')

# cierro el archivo
f.close()

# ------------------------------------------------

# abro el archivo previamente creado
f = open("data.txt")

# leo lo que tiene el archivo y lo almaceno en la variable result
result = f.read()

# cierro el archivo
f.close()

# imprimo el resultado (debería ser la leyenda)
print(result)

# ------------------------------------------------

# traigo os
import os

# listo los archivos del directorio actual
os.listdir()

# ------------------------------------------------


# creo un directiorio
os.mkdir('dir')

# listo el directorio actual para verificar la creación
os.listdir()

# elimino el directorio
os.rmdir("dir")

# ------------------------------------------------

# elimino el primer archivo
os.remove('data.txt')