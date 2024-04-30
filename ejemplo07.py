diccionario={}
diccionario['nombres']="Stefany"
diccionario['apellidos']="Pedroza Rodriguez"
diccionario['ciudad']="Loja"

#accede al diccionario 
print(diccionario.keys())

#presentar todos los valores de las llaves a los diccionarios
for x in diccionario.keys(): #la primera vez va a dar el nombre que es el valor de x
    print(diccionario[x])