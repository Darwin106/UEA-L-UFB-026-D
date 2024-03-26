# Escribiendo en el archivo
with open("my_notes.txt", "w") as my_notes:
    # Write notes to the file
    my_notes.write("Hola me gusta programar\n")
    my_notes.write("Soy estudiante de uea\n")
    my_notes.write("Este es el ultimo trabajo\n")

# Se realiza la lectura de archivo

print("Leyendo los archivos de se encuentra en my_notes.txt: \n ")

with open("my_notes.txt", "r") as my_notes:
    # Leer e imprimir líneas
    line = my_notes.readline()
    while line:
        print(line.strip())
        line = my_notes.readline()

# cerrar el archivo
my_notes.close()