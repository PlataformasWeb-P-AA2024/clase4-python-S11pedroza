archivo=open("data/atp_tennis.csv","r")

Lineas=archivo.readlines()

#listas compresas
Lineas=[l.split("|") for l in Lineas] #La cadena se convirtio en una lista gracias al split

for x in Lineas:
    cadena="""<b>Torneo:</b> %s <br> <b>Ganador:</b> %s""" % (x[0],x[9])
    print(cadena)
    archivo_generado=open("data/%s.html" % (x[9]),"w") #debe salirme 25363 archivos con nombres unicos
    archivo_generado.writelines("%s\n" % (cadena))
    archivo_generado.close()