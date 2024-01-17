#Toda lista se debe escribir en PLURAL
arboles=['ceiba', 'yarumo', 'manzano','guayacan']

municipios=["Medellin", "titiribi","Carolina del principe"]

hectareaSembradas=[2500, 500, 1200]

lluviasMayoresA500= [False, True, True]

#Recorriendo un arreglo...
#Acceder de FORMA DINAMICA el contenido de un arreglo
#Para RECORRERLO DEBO UTILIZAR UN CICLO O BUCLE O LOOP

#ciclo while (mientras)
'''contador= 0
while contador <10 :
    contador= contador+1
    print("estoy triunfando...")'''

#Ciclo For (Para)
'''for variableiteradora in range(0, 301,2):
    print(variableiteradora)'''

#Recorrer dinamicamente un arreglo usando un foreach (PARA CADA UNO)
for municipio in municipios:
    print(municipio)
