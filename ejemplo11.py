import uuid

archivo = open("data/atp_tennis.csv", "r")
lineas = archivo.readlines()
#listas compresas
lineas = [l.split("|") for l in lineas] #La cadena se convirtio en una lista gracias al split

for x in lineas:
    cadena="""<b>Torneo:</b> %s <br> <b>Ganador:</b> %s""" % (x[0],x[9])
    
    # Generar un identificador único para el nombre del archivo
    nombre_archivo = str(uuid.uuid4()) + ".html"
    
    # Crear el archivo con el nombre único
    archivo_generado = open("data/" + nombre_archivo, "w")
    archivo_generado.write("%s\n" % cadena)
    archivo_generado.close()