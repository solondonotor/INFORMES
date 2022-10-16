################# EJERCICIO 1 #####################

#Planteamos una matriz con los puntos a evaular

from operator import index
from platform import java_ver


P = [['p1', 2,   2,    3], 
     ['p2', 2,   3,    4], 
     ['p3', 1,   1,    3], 
     ['p4', 0.5, 0.5,  2], 
     ['p5', 1,   2,    1],
     ['p6', 1,   0.5,  1],
     ['p7', 3,   2,  0.5],
     ['p8', 3,   1,    2],
     ['p9', 0,   0,    0],
     ['p10', 2,  0,    0.5]]

# Buscamos el punto a menor distancia para cada punto
distancias =[]
Parescercanos = []
for i in range(0, 10):
    d = 100
    for k in range(0, 10):
        if k != i:
            dx = P[i][1] - P[k][1] 
            dy = P[i][2] - P[k][2]
            dz = P[i][3] - P[k][3]
            di = (dx**2 + dy**2 + dz**2)**0.5
            if di < d:
                d = di
                num = k+1
    parCercano1 = "P" + str(i+1) + "-P" + str(num)   # Almacenamos la respuesta en un string
    Parescercanos += [parCercano1]
    distancias += [d]
    #print(parCercano1, round(d, 2))                              # Mostramos los puntos cercanos con su distancia


Minima_distancia = (min(distancias))
p = distancias.index(Minima_distancia)

parCercano = Parescercanos[p]
#print(parCercano)
 ##################### EJERCICIO 2 ############################

# 1. lista1 = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]

n = 0
i = -1
Sec1 = []
while n < 26:
    i = i * -1
    n += 1
    Sec1.append(i) 
# print(Sec1)
 
# 2. lista2 = [100, -1, 99, -1, 98, -1, 97, -1, 96, -1, ... 3, -1, 2, -1, 1, -1]

n1 = 101
Sec2 = []
while n1 > 1:
    n1 = n1 - 1
    Sec2.append(n1)
    Sec2.append(-1)
# print(Sec2)

#3. lista3 = [2, 4, 5, 6, 8, 10,12, 14,15, 16,18, 20, 22, 24, 25 ... 592, 594, 595 ,596 ,598, 600]

n2= 0
Sec3 = []
while n2 < 601:
    n2 = n2 + 1
    if n2 % 2 == 0:
        Sec3.append(n2)
    elif n2 % 5 == 0:
        Sec3.append(n2)
print(Sec3)

listaDeListas = [Sec1, Sec2, Sec3]

########################## EJERCICIO 3 ############################

# Definimos un diccionario con los nombres de los estudiantes como claves y les asignamos sus notas las definimos
# como una lista.
Notas = {'Miguel Pineda': [1.0, 1.1, 2.3, 1.1], 'Maria Gonzalez': [3.1, 3.1, 1.2, 3.0], 
'Jose Nuñez': [5.0, 4.0, 2.5, 5.0], 'Angelica Lozano': [3.1, 1.0, 2.6, 1.0], 
'Camilo Suarez': [3.2, 4.0, 1.1, 3.0], 'Mariana Rosero' : [5.0, 5.0, 5.0, 3.9],
'Esteban Quesada': [3.4, 4.0, 2.6, 3.2], 'Julia Quintero': [2.0, 2.2, 2.1, 4.2],
'Mauricio Lizcano': [3.7, 4.1, 4.7, 4.4, 5.0], 'Angie Gomez': [4.1, 4.7, 4.4, 5.0],
'Camilo Restrepo': [5.0, 5.0, 1.0, 3.2], 'Mauricio Velazques': [5.0, 4.2, 2.1, 5.0],
'Esteban Rodriguez': [3.2, 4.1, 2.2, 3.3] }

# 1. Miramos cuantos pierden así saquen 5 en su próxima nota, para esto, primero les añadimos la ultima nota en 5 a todos
matxnotas = list(Notas.values()) # Creamos una matriz con las notas.

# Para calcular las definitivas asumiendo que todos saquen 5 en la ultima
i = 0
definitiva = []
while i < 13:
    matxnotas[i].append(5.0)                            # Se hace un ciclo donde se añade la quinta nota como 5
    nota1 = matxnotas[i][0]*0.1                         # Se calcula el valor total de cada nota
    nota2 = matxnotas[i][1]*0.2
    nota3 = matxnotas[i][2]*0.15
    nota4 = matxnotas[i][3]*0.2
    nota5 = matxnotas[i][4]*0.35
    sumdef = nota1 + nota2 + nota3 + nota4 + nota5      # Se suma el total de notas
    definitiva += [round(sumdef, 2)]                    # Creamos una nueva lista donde se almacenan las definitvas
    i += 1

# Para calcular las notas asumiendo que sacan 0 en la ultima nota:
j = 0
definitiva2 = []
while i < 13:
    matxnotas[i].append(0.0)                            # Se hace un ciclo donde se añade la quinta nota como 0
    nota1 = matxnotas[i][0]*0.1                         # Se calcula el valor total de cada nota
    nota2 = matxnotas[i][1]*0.2
    nota3 = matxnotas[i][2]*0.15
    nota4 = matxnotas[i][3]*0.2
    nota5 = matxnotas[i][4]*0.35
    sumdef = nota1 + nota2 + nota3 + nota4 + nota5      # Se suma el total de notas
    definitiva2 += [round(sumdef, 2)]                    # Creamos una nueva lista donde se almacenan las definitvas
    j += 1

Notas1 = Notas # Nuevo diccionario con las definitivas si sacaran 5
Notas1['Miguel Pineda'] = definitiva[0]
Notas1['Maria Gonzalez'] = definitiva[1]
Notas1['Jose Nuñez'] = definitiva[2]
Notas1['Angelica Lozano'] = definitiva[3]
Notas1['Camilo Suarez'] = definitiva[4]
Notas1['Mariana Rosero'] = definitiva[5]
Notas1['Esteban Quesada'] = definitiva[6]
Notas1['Julia Quintero'] = definitiva[7]
Notas1['Mauricio Lizcano'] = definitiva[8]
Notas1['Angie Gomez'] = definitiva[9]
Notas1['Camilo Restrepo'] = definitiva[10]
Notas1['Mauricio Velazques'] = definitiva[11]
Notas1['Esteban Rodriguez'] = definitiva[12]

Notas2 = Notas # Nuevo diccionario con las definitivas si sacaran 0
Notas2['Miguel Pineda'] = definitiva[0]
Notas2['Maria Gonzalez'] = definitiva[1]
Notas2['Jose Nuñez'] = definitiva[2]
Notas2['Angelica Lozano'] = definitiva[3]
Notas2['Camilo Suarez'] = definitiva[4]
Notas2['Mariana Rosero'] = definitiva[5]
Notas2['Esteban Quesada'] = definitiva[6]
Notas2['Julia Quintero'] = definitiva[7]
Notas2['Mauricio Lizcano'] = definitiva[8]
Notas2['Angie Gomez'] = definitiva[9]
Notas2['Camilo Restrepo'] = definitiva[10]
Notas2['Mauricio Velazques'] = definitiva[11]
Notas2['Esteban Rodriguez'] = definitiva[12]

Cantidad_que_pierden = 0 #Contamos cuantos pierden
for word, meaning in Notas1.items():
    if meaning <= 3: #Miramos quienes pierden
        Cantidad_que_pierden += 1
        #print(f'{word}:{meaning}') 
#print(Cantidad_que_pierden) #Cantidad de estudiantes que pierden así saquen 5

Cantidad_que_ganan = 0 #Contamos cuantos ganan
for word, meaning in Notas1.items():
    if meaning >= 3: #Miramos quienes ganan
        Cantidad_que_ganan += 1
        print(f'{word}:{meaning}') 
#print(Cantidad_que_ganan) #Cantidad de estudiantes que ganan así saquen 0

#Para calular los que tienen posibilidades le restamos al total de estudiantes
#Los que ni sacando 5 pasan
Cantidad_con_posibilidades = 13 - Cantidad_que_pierden

estudiantes= [Cantidad_que_pierden, Cantidad_que_ganan, Cantidad_con_posibilidades]
print(estudiantes)

###################### EJERCICIO 4 ##########################
#Planteamos un diccionario donde se le asignará a cada persona un lista con los dias de la
# semana que va, siendo 1 sí y 0 no.
UsosTaxi_Ida = {'Juan': [1, 1, 1, 1, 0 ], 'Camila':[ 1, 0, 1, 0, 1],
 'Jose': [1 ,0 ,1 ,1 ,0], 'Maria': [1, 1, 1, 0, 0], 
 'Esteban': [1, 0, 0, 1, 1], 'Angie': [1, 0, 1, 0, 0]}

UsosTaxi_Vuelta = {'Juan': [1, 1, 1, 0, 0 ], 'Camila': [1, 0, 0, 0, 0],
 'Jose': [1 ,0 ,1 ,1 ,0], 'Maria': [0, 0, 1, 0, 0], 
 'Esteban': [0, 0, 0, 1, 0], 'Angie': [1, 0, 1, 0, 0]}

#Creamos un diccionario donde se irán acumulando lo que debe ir pagando cada persona
diccionarioPagos = {'Juan': 0, 'Camila':0,  'Jose': 0, 'Maria': 0, 'Esteban': 0, 'Angie': 0}



#____________Calculo de Ida:

totxdia_Ida = [] # Total de cuantos de van por dia, asignados en una lista [Lunes, Martes, Miercoles...]
usosxpersona_I = list(UsosTaxi_Ida.values()) # Casteamos las listas de los valores del diccionario para
                                            # Crear una lista con las listas.

#Calculo del total de personas que van por día
for i in range (0,5):                       #Recorremos los días de la semana
    totxdia = 0
    for j in range(0,6):                    #Recorremos las personas
        totxdia += usosxpersona_I[j][i]     # Se acumula cada persona que va por cada día
    totxdia_Ida += [totxdia]

'''    
Recorremos el diccionario de Usos de Ida, y miramos quien usa el taxi el primer día, 
dividimos los 15000 de tarifa entre el total de gente que va por día y se los sumamos al 
Saldo de esa persona
'''

for word, meaning in UsosTaxi_Ida.items():      # Recorremos cada persona
    for i in range(0, 5):                       # Recorremos los dias de la semana
        if meaning[i] == 1:                     # Si la persona va 
            v = 15000/totxdia_Ida[i]            # Se reparte entre los que van 
            diccionarioPagos[word] += round(v, 2)         # Y se los sumamos a la cuenta
        elif totxdia_Ida[i] == 0:               # Si nadie va ese día
            diccionarioPagos[word] += round(10000/6, 2)   # Se reparte el gasto

#Calculo de Vuelta: Se repite el procedimiento

totxdia_V = []
usosxpersona_V = list(UsosTaxi_Vuelta.values())

for i in range (0,5):
    totxdia = 0
    for j in range(0,6):
        totxdia += usosxpersona_V[j][i]
    totxdia_V += [totxdia]
    
for word, meaning in UsosTaxi_Vuelta.items():
    for i in range(0, 5):
        if meaning[i] == 1:
            v = 15000/totxdia_V[i]
            diccionarioPagos[word] += v
        elif totxdia_V[i] == 0:
            diccionarioPagos[word] += 10000/6

print(diccionarioPagos)


############# EJERCICIO 5 ###############

# Lista de los empleados con sus ventas respectivas
# [codigo, zapatos, tenis, camisas, corbatas, pantalones, blusas, vestidos]
Ventas= [[1, 20, 22, 30, 2, 40, 20, 3], 
         [2, 31, 14, 32, 15, 13, 20, 11], 
         [10, 24, 32, 40, 9, 12, 50, 13], 
         [20, 42, 12, 33, 24, 22, 32, 23],
         [21, 51, 21, 25, 10, 19, 14, 2], 
         [22, 22, 31, 52, 21, 35, 15, 11],
         [23, 21, 36, 22, 32, 39, 32, 15], 
         [24, 22, 33, 41, 21, 43, 31, 36],
         [25, 33, 31, 20, 42, 33, 42, 35], 
         [31, 22, 47, 5, 28, 37, 31, 32],
         [32, 24, 38, 33, 21, 41, 31, 16], 
         [33, 21, 18, 32, 37, 39, 22, 12],
         [41, 33, 31, 21, 21, 33, 39, 25], 
         [42, 25, 39, 20, 48, 15, 30, 32],
         [43, 27, 32, 29, 28, 27, 35, 16], 
         [121, 24, 12, 31, 21, 39, 32, 13],
         [122, 31, 31, 50, 22, 13, 30, 21], 
         [123, 23, 35, 35, 39, 31, 19, 19],
         [151, 26, 36, 39, 27, 35, 32, 16], 
         [352, 25, 31, 21, 21, 25, 37, 15],
         [353, 23, 34, 35, 32, 37, 20, 49], 
         [368, 31, 14, 29, 39, 25, 37, 16],
         [369, 26, 31, 31, 27, 37, 32, 41], 
         [461, 40, 42, 23, 11, 21, 15, 19],
         [466, 27, 31, 39, 21, 31, 32, 25],
         [469, 38, 32, 19, 29, 35, 50, 16]]


Saldos = [round(1200000*(1+0.05+0.1), 2)]*len(Ventas) # Nueva Lista con los saldos para cada empleado

#Calculo de la comision
for i in range(len(Ventas)):
    Comision = (Ventas[i][1]*(50)*0.05 + Ventas[i][2]*(70)*0.04 + Ventas[i][3]*(40)*0.06 
    + Ventas[i][4]*(25)*0.07 + Ventas[i][5]*(35)*0.05 + Ventas[i][6]*(80)*0.03 + 
    Ventas[i][7]*(95)*0.02)
    Saldos[i] += round(Comision*1000, 2)

codigosAltosSalarios = []

for j in range(0, 3):                   #Busca los 3 primeros con mayor saldo
    for n in range(len(Ventas)):        # Recorre la lista buscando el máximo
        if Saldos[n] == max(Saldos):    # Cuando encuentre el máximo
            codigosAltosSalarios += [Ventas[n][0]]     #Identifica a que codigo pertenece y le asigna el saldo
            Saldos[n] = 0               #Renueva el máximo como 0 para que busque el siguiente
            break                       # Se rompe el ciclo cuando encuentre el máximo

print(codigosAltosSalarios)





 


