nombre_completo = 'Sofia Londoño Toro'

#____________ EJERCICIO 1 ___________________

precios_dict = {'A001': 31000,
           'A011': 25000,  
           'A032': 43000,  
           'A125': 55000,  
           'B001': 10000,  
           'B005': 20000,  
           'P009': 30000,  
           'P019': 49000,  
           'R001': 60000,  
           'W307': 90000,
           'Z025': 27000,  
           'Z052': 35000,  
           'Z278': 65000}

precios = list(precios_dict.values())
articulos = list(precios_dict.keys())


ventas = ["A032-52Unidades", "B001-29Unidades", 
          "A125-15Unidades", "A032-22Unidades",
          "P009-25Unidades", "B005-20Unidades", 
          "B001-19Unidades", "P009-31Unidades", 
          "B005-22Unidades", "W307-15Unidades", 
          "A011-31Unidades", "P019-18Unidades", 
          "A011-20Unidades", "R001-20Unidades", 
          "P019-19Unidades", "A001-12Unidades", 
          "A125-20Unidades", "R001-31Unidades", 
          "Z052-52Unidades", "W307-31Unidades", 
          "Z025-42Unidades", "Z052-10Unidades", 
          "Z278-30Unidades", "Z025-24Unidades", 
          "Z278-21Unidades", "A001-31Unidades",
          "A032-32Unidades", "B001-22Unidades",
          "A125-11Unidades", "A032-12Unidades",
          "P009-19Unidades", "B005-11Unidades",
          "B001-19Unidades", "P009-21Unidades",
          "B005-22Unidades", "W307-15Unidades",
          "A011-31Unidades", "P019-18Unidades",
          "A011-20Unidades", "R001-20Unidades",
          "P019-19Unidades", "A001-12Unidades",
          "A125-20Unidades", "R001-31Unidades",
          "Z052-12Unidades", "W307-31Unidades",
          "Z025-42Unidades", "Z052-10Unidades",
          "Z278-30Unidades", "Z025-24Unidades",
          "Z278-11Unidades", "A001-91Unidades"]

ventas1 = sorted(ventas)   # Ordenamos alfabeticamente la base de datos
unidades = [ ventas1[:4],  # Hacemos una lista con las listas por cada dato del elemento
             ventas1[4:8],
             ventas1[8:12],
             ventas1[12:16],
             ventas1[16:20],
             ventas1[20:24],
             ventas1[24:28],
             ventas1[28:32],
             ventas1[32:36],
             ventas1[36:40],
             ventas1[40:44],
             ventas1[44:48],
             ventas1[48:52]]



unidadesN = [] # Separamos los cogidos de los productos del resto del str
for codxunid in unidades:
    codigo=[]
    for i in codxunid:
        elemento = i.split(sep = '-')
        codigo += [elemento] 
    unidadesN += [codigo]


unidadesNN = [] #Dejamos solo cuanto se vendió por atículo 
for j in unidadesN:
    soporte = []
    for k in j:
        elemento_nuevo =[]
        for i in k:
           elemento_nuevo += [i.replace('Unidades', '')]
        soporte += [elemento_nuevo]
    unidadesNN += [soporte] 
      

for i in unidadesNN: # Eliminamos el nombre del articulo
    for j in i:
        j.pop(0)

unidadesNNN = [] #Quitamos el numero del artículo de las listas
for i in unidadesNN:
    a = []
    for j in i:
        a += j
    unidadesNNN += [a]
unidadesNNNN = []
for i in unidadesNNN: #Convertimos los datos en flotantes
    nuevL =[]
    for j in i:
       nuevL.append(float(j))
    unidadesNNNN.append(nuevL)


unidades_totales = [] # Sumamos los items por cada articulo
for i in unidadesNNNN:
    uni = sum(i)
    unidades_totales += [uni]

unidadesxprecios = [x*y for x,y in zip(precios,unidades_totales)] #Sacamos los totales por producto
ventasTotal = sum(unidadesxprecios) #Totalizamos las ventas
unidadesPorProducto = dict(zip(articulos, unidades_totales)) #Creamos el diccionario de unidades por producto
ventasPorProducto = dict(zip(articulos, unidadesxprecios)) #Creamos el diccionario de total de ventas por producto

reporteVentas = [unidadesPorProducto, ventasPorProducto, ventasTotal]

#____________ EJERCICIO 2 ___________________

calificaciones = {
                      "001": {"Nombre": "Cristian Pachon",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.2,   "Artes": 4.0,  "Musica": 0.5},
                      "002": {"Nombre": "Daniela Pineda",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 4.0,   "Artes": 3.1,  "Musica": 4.0},
                      "003": {"Nombre": "Esteban Murcia",       "Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 3.1,   "Artes": 0.0,  "Musica": 3.1},
                      "004": {"Nombre": "Jose Guzman",          "Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.2,  "Musica": 0.0},
                      "005": {"Nombre": "Camilo Rodriguez",     "Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 1.0,  "Musica": 0.2},
                      "006": {"Nombre": "Mariana Londoño",      "Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.3,  "Musica": 1.0},
                      "007": {"Nombre": "Estefania Muños",      "Fisica":  5.0,   "Ingles": 1.2,   "Deportes": 1.2,   "Artes": 1.9,  "Musica": 1.3},
                      "008": {"Nombre": "Cristian Rodriguez",   "Fisica":  0.2,   "Ingles": 2.9,   "Deportes": 1.0,   "Artes": 4.2,  "Musica": 1.9},
                      "009": {"Nombre": "Natalia Alzate",       "Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                      "010": {"Nombre": "Juan Sanabria",        "Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                      "011": {"Nombre": "Juanita Calderon",     "Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 0.5,  "Musica": 4.2},
                      "012": {"Nombre": "Laura Quintero",       "Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 4.2,   "Artes": 0.0,  "Musica": 0.5},
                      "013": {"Nombre": "Viviana Quesada",      "Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 2.3,   "Artes": 4.2,  "Musica": 0.0},
                      "014": {"Nombre": "Camila Alzate",        "Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 2.5,   "Artes": 4.3,  "Musica": 3.2},
                      "015": {"Nombre": "Leonidas Sanabria",    "Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 4.2,   "Artes": 2.5,  "Musica": 4.3},
                      "016": {"Nombre": "Juana Diaz",           "Fisica":  4.1,   "Ingles": 0.0,   "Deportes": 4.5,   "Artes": 4.2,  "Musica": 2.5},
                      "017": {"Nombre": "Laura Playonero",      "Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 0.5,   "Artes": 4.5,  "Musica": 3.2},
                      "018": {"Nombre": "Viviana Restrepo",     "Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                      "019": {"Nombre": "Elias Rodriguez",      "Fisica":  2.2,   "Ingles": 0.5,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                      "020": {"Nombre": "Mariana Pacheco",      "Fisica":  2.0,   "Ingles": 2.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                      "021": {"Nombre": "Estefany Muñoz",       "Fisica":  2.2,   "Ingles": 1.0,   "Deportes": 3.1,   "Artes": 4.0,  "Musica": 4.0},
                      "022": {"Nombre": "Cristian Fernandez",   "Fisica":  2.9,   "Ingles": 4.2,   "Deportes": 0.0,   "Artes": 3.1,  "Musica": 3.1},
                      "023": {"Nombre": "Jessika Arias",        "Fisica":  2.0,   "Ingles": 4.0,   "Deportes": 4.0,   "Artes": 0.0,  "Musica": 0.2},
                      "024": {"Nombre": "Juan Mendoza",         "Fisica":  4.5,   "Ingles": 4.2,   "Deportes": 4.0,   "Artes": 4.2,  "Musica": 0.5},
                      "025": {"Nombre": "Maria Calderon",       "Fisica":  2.2,   "Ingles": 0.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 1.0},
                      "026": {"Nombre": "Laura Lozada",         "Fisica":  2.0,   "Ingles": 5.0,   "Deportes": 1.0,   "Artes": 1.0,  "Musica": 1.3},
                      "027": {"Nombre": "Yessica Quesada",      "Fisica":  1.2,   "Ingles": 5.0,   "Deportes": 1.9,   "Artes": 1.2,  "Musica": 1.3},
                      "028": {"Nombre": "Jennifer Alzate",      "Fisica":  2.9,   "Ingles": 0.2,   "Deportes": 4.2,   "Artes": 1.0,  "Musica": 1.9},
                      "029": {"Nombre": "Karen Sanabria",       "Fisica":  0.0,   "Ingles": 4.1,   "Deportes": 4.2,   "Artes": 4.5,  "Musica": 2.5},
                      "030": {"Nombre": "Fernando Rodriguez",   "Fisica":  0.5,   "Ingles": 2.2,   "Deportes": 0.2,   "Artes": 0.2,  "Musica": 4.1},
                      "031": {"Nombre": "Nina Londoño",         "Fisica":  4.2,   "Ingles": 4.2,   "Deportes": 2.5,   "Artes": 4.2,  "Musica": 4.3},
                      "032": {"Nombre": "Favio Munera",         "Fisica":  5.0,   "Ingles": 2.3,   "Deportes": 2.9,   "Artes": 2.9,  "Musica": 0.2},
                      "033": {"Nombre": "Lindsey Roy",          "Fisica":  4.2,   "Ingles": 5.0,   "Deportes": 4.2,   "Artes": 4.2,  "Musica": 3.9},
                      "034": {"Nombre": "Nathalia Hernandez",   "Fisica":  4.2,   "Ingles": 4.5,   "Deportes": 0.0,   "Artes": 4.2,  "Musica": 0.5},
                      "035": {"Nombre": "Juan Gaviria",         "Fisica":  0.5,   "Ingles": 0.5,   "Deportes": 4.2,   "Artes": 2.3,  "Musica": 0.0},
                      "036": {"Nombre": "Fabio Urrego",         "Fisica":  4.1,   "Ingles": 3.1,   "Deportes": 4.3,   "Artes": 2.5,  "Musica": 3.2},
                      "037": {"Nombre": "Fernanda Quintero",    "Fisica":  0.5,   "Ingles": 0.2,   "Deportes": 4.1,   "Artes": 4.1,  "Musica": 4.5},
                      "038": {"Nombre": "Camila Queiroz",       "Fisica":  1.2,   "Ingles": 3.1,   "Deportes": 4.5,   "Artes": 0.5,  "Musica": 3.2},
                      "039": {"Nombre": "Ursula Alzate",        "Fisica":  2.2,   "Ingles": 4.0,   "Deportes": 4.2,   "Artes": 0.5,  "Musica": 2.0},
                      "040": {"Nombre": "Aureliano Buendia",    "Fisica":  1.0,   "Ingles": 3.1,   "Deportes": 4.0,   "Artes": 4.0,  "Musica": 2.2},
                }

listaNombres = [] #Creamos una lista con los nombres
for cod in calificaciones.keys():
    listaNombres.append(calificaciones[cod]['Nombre'])



promediosxest= [] # Calculamos los promedios
for cod in calificaciones.keys():
    Promxest = (calificaciones[cod]['Fisica'] + calificaciones[cod]['Deportes'] +
            calificaciones[cod]['Ingles'] +calificaciones[cod]['Artes'] +
            calificaciones[cod]['Musica'])/5
    promediosxest.append(round(Promxest,2))

promediosPorEstudiante = dict(zip(listaNombres, promediosxest)) #Creamos el diccionario

estudiantesAprobados = [] #Lista de nombres de aprobados
estudiantesReprobados = []
listapromedios = list(promediosPorEstudiante.values())
i= 0

for est in listapromedios:
    estudiante = str(list(promediosPorEstudiante.keys())[listapromedios.index(est)])
    if est >= 3.0:
        estudiantesAprobados.append(estudiante)
    elif 0 < est < 3.0:
        estudiantesReprobados.append(estudiante)
    listapromedios[i]= 0
    i+=1

#Para sacar promedios por asignatura:
acumIngles = 0
acumDeportes = 0
acumFisica = 0
acumArtes = 0
acumMusica = 0

for cod in calificaciones.keys():
    acumIngles +=   calificaciones[cod]['Ingles']
    acumDeportes += calificaciones[cod]['Deportes']
    acumFisica +=  calificaciones[cod]['Fisica']
    acumArtes += calificaciones[cod]['Artes']
    acumMusica +=  calificaciones[cod]['Musica']

PromxIngles   = round(acumIngles / len(calificaciones), 2)
PromxDeportes = round(acumDeportes / len(calificaciones), 2)
PromxFisica   = round(acumFisica / len(calificaciones), 2)
PromxArtes    = round(acumArtes / len(calificaciones), 2)
PromxMusica   = round(acumMusica / len(calificaciones), 2)

listaNombresMaterias = ['Ingles','Deportes', 'Fisica', 'Artes', 'Musica']
promediosxasignatura = [PromxIngles, PromxDeportes, PromxFisica, PromxArtes, PromxMusica]
promediosPorMateria = dict(zip(listaNombresMaterias, promediosxasignatura))


reporteEstudiantes = [promediosPorEstudiante, promediosPorMateria, estudiantesAprobados, estudiantesReprobados]



#____________ EJERCICIO 3 ___________________

costosCine = {'2D': {'NIÑO':{'LUN-VIE' : 5000.0, 'SAB-DOM': 7000.0}, 'ADULTO': {'LUN-VIE' : 8000.0, 'SAB-DOM': 9000.0}},
              '3D': {'NIÑO':{'LUN-VIE' : 8000.0, 'SAB-DOM': 9000.0}, 'ADULTO': {'LUN-VIE' : 12000.0, 'SAB-DOM': 15000.0}}}


VentasCine = [
   ("2D_3NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_1ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_1ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("2D_0NIÑOS_LUNES", "2D_2ADULTOS_LUNES"),("3D_0NIÑOS_LUNES", "3D_3ADULTOS_LUNES"),("3D_3NIÑOS_LUNES", "3D_4ADULTOS_LUNES"),("2D_2NIÑOS_LUNES", "2D_4ADULTOS_LUNES"),("2D_1NIÑOS_MARTES",
    "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),
   ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),(
       "2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_3NIÑOS_MARTES", "3D_2ADULTOS_MARTES"),
   ("2D_3NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_1ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("2D_0NIÑOS_MARTES", "2D_2ADULTOS_MARTES"),("3D_0NIÑOS_MARTES", "3D_3ADULTOS_MARTES"), ("3D_3NIÑOS_MARTES", "3D_4ADULTOS_MARTES"),("2D_2NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),(
       "2D_1NIÑOS_MARTES", "2D_4ADULTOS_MARTES"),("3D_1NIÑOS_MARTES", "3D_1ADULTOS_MARTES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES",
    "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_0NIÑOS_MIERCOLES", "3D_3ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("2D_1NIÑOS_MIERCOLES", "2D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),
   ("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("2D_0NIÑOS_MIERCOLES", "2D_2ADULTOS_MIERCOLES"),("3D_3NIÑOS_MIERCOLES", "3D_4ADULTOS_MIERCOLES"),("3D_1NIÑOS_MIERCOLES", "3D_1ADULTOS_MIERCOLES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
       "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),(
       "2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),(
       "2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),
   ("3D_3NIÑOS_JUEVES", "3D_4ADULTOS_JUEVES"),("2D_2NIÑOS_JUEVES", "2D_1ADULTOS_JUEVES"),("2D_0NIÑOS_JUEVES", "2D_2ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("3D_2NIÑOS_JUEVES", "3D_1ADULTOS_JUEVES"),("3D_0NIÑOS_JUEVES", "3D_3ADULTOS_JUEVES"),("2D_3NIÑOS_JUEVES", "2D_4ADULTOS_JUEVES"),("2D_1NIÑOS_JUEVES", "2D_0ADULTOS_JUEVES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES",
    "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_2NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES", "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_1ADULTOS_VIERNES"),("3D_1NIÑOS_VIERNES",
    "3D_1ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_0ADULTOS_VIERNES"),("2D_0NIÑOS_VIERNES", "2D_2ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("3D_0NIÑOS_VIERNES", "3D_3ADULTOS_VIERNES"),("3D_3NIÑOS_VIERNES", "3D_4ADULTOS_VIERNES"),("2D_2NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),
   ("2D_1NIÑOS_VIERNES", "2D_4ADULTOS_VIERNES"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),(
       "3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("3D_1NIÑOS_SABADO", "3D_1ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),
   ("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),(
       "2D_1NIÑOS_SABADO", "2D_0ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),
   ("2D_1NIÑOS_SABADO", "2D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO", "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_SABADO", "2D_1ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("2D_0NIÑOS_SABADO", "2D_2ADULTOS_SABADO"),("3D_0NIÑOS_SABADO", "3D_3ADULTOS_SABADO"),("3D_3NIÑOS_SABADO",
    "3D_4ADULTOS_SABADO"),("2D_1NIÑOS_DOMINGO", "2D_0ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"), ("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO",
    "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_2ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_3ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO",
    "3D_2ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO", "2D_4ADULTOS_DOMINGO"),("2D_1NIÑOS_DOMINGO", "2D_1ADULTOS_DOMINGO"),("3D_2NIÑOS_DOMINGO", "3D_4ADULTOS_DOMINGO"),("3D_0NIÑOS_DOMINGO", "3D_5ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_0ADULTOS_DOMINGO"),
   ("3D_0NIÑOS_DOMINGO", "3D_3ADULTOS_DOMINGO"),("2D_3NIÑOS_DOMINGO",
    "2D_4ADULTOS_DOMINGO"),("3D_1NIÑOS_DOMINGO", "3D_9ADULTOS_DOMINGO")
]

Ventas2D = []       
Ventas3D = []
for item in VentasCine:
    for i in item:
        if i[0] == '2':
            Ventas2D.append(i)
        elif i[0] == '3':
            Ventas3D.append(i)

Ventas2DNiños = []
Ventas2DAdultos = []
for item in Ventas2D:
    if item[4] == 'N':
        Ventas2DNiños.append(item)
    elif item[4] == 'A':
        Ventas2DAdultos.append(item)
      

VENTAS_2D_ADULTOS_LUNES     = []
VENTAS_2D_ADULTOS_MARTES    = []
VENTAS_2D_ADULTOS_MIERCOLES = []
VENTAS_2D_ADULTOS_JUEVES    = []
VENTAS_2D_ADULTOS_SABADO    = []
VENTAS_2D_ADULTOS_DOMINGO   = []
VENTAS_2D_ADULTOS_VIERNES   = []
for item in Ventas2DAdultos:
    if item[12] == 'L':
        VENTAS_2D_ADULTOS_LUNES.append(item)
    elif item[14] == 'R':
        VENTAS_2D_ADULTOS_MARTES.append(item)
    elif item[16] == 'C':
        VENTAS_2D_ADULTOS_MIERCOLES.append(item)
    elif item[12] == 'J':
        VENTAS_2D_ADULTOS_JUEVES.append(item)
    elif item[12] == 'V':
        VENTAS_2D_ADULTOS_VIERNES.append(item)
    elif item[12] == 'S':
        VENTAS_2D_ADULTOS_SABADO.append(item)
    elif item[12] == 'D':
        VENTAS_2D_ADULTOS_DOMINGO.append(item)

VENTAS_2D_NIÑOS_LUNES     = []
VENTAS_2D_NIÑOS_MARTES    = []
VENTAS_2D_NIÑOS_MIERCOLES = []
VENTAS_2D_NIÑOS_JUEVES    = []
VENTAS_2D_NIÑOS_SABADO    = []
VENTAS_2D_NIÑOS_DOMINGO   = []
VENTAS_2D_NIÑOS_VIERNES   = []
for item in Ventas2DNiños:
    if item[10] == 'L':
        VENTAS_2D_NIÑOS_LUNES.append(item)
    elif item[12] == 'R':
        VENTAS_2D_NIÑOS_MARTES.append(item)
    elif item[14] == 'C':
        VENTAS_2D_NIÑOS_MIERCOLES.append(item)
    elif item[10] == 'J':
        VENTAS_2D_NIÑOS_JUEVES.append(item)
    elif item[10] == 'V':
        VENTAS_2D_NIÑOS_VIERNES.append(item)
    elif item[10] == 'S':
        VENTAS_2D_NIÑOS_SABADO.append(item)
    elif item[10] == 'D':
        VENTAS_2D_NIÑOS_DOMINGO.append(item)

listaVentas2D_Niños = [  VENTAS_2D_NIÑOS_LUNES ,   
                         VENTAS_2D_NIÑOS_MARTES   ,
                         VENTAS_2D_NIÑOS_MIERCOLES,
                         VENTAS_2D_NIÑOS_JUEVES   ,
                         VENTAS_2D_NIÑOS_VIERNES,
                         VENTAS_2D_NIÑOS_SABADO   ,
                         VENTAS_2D_NIÑOS_DOMINGO]


listaVentas2D_Adultos = [VENTAS_2D_ADULTOS_LUNES ,   
                         VENTAS_2D_ADULTOS_MARTES   ,
                         VENTAS_2D_ADULTOS_MIERCOLES,
                         VENTAS_2D_ADULTOS_JUEVES   ,
                         VENTAS_2D_ADULTOS_VIERNES ,
                         VENTAS_2D_ADULTOS_SABADO   ,
                         VENTAS_2D_ADULTOS_DOMINGO ]

Ventasxdia2D_Adultos = []
for dia in listaVentas2D_Adultos:
    listadeApoyo =[]
    for item in dia:
        listadeApoyo.append(int(item[3]))
    Ventasxdia2D_Adultos.append(sum(listadeApoyo))

Ventasxdia2D_Niños = []
for dia in listaVentas2D_Niños:
    listadeApoyo =[]
    for item in dia:
        listadeApoyo.append(int(item[3]))
    Ventasxdia2D_Niños.append(sum(listadeApoyo))

Ventas3DNiños = []
Ventas3DAdultos = []
for item in Ventas3D:
    if item[4] == 'N':
        Ventas3DNiños.append(item)
    elif item[4] == 'A':
        Ventas3DAdultos.append(item)
      

VENTAS_3D_ADULTOS_LUNES     = []
VENTAS_3D_ADULTOS_MARTES    = []
VENTAS_3D_ADULTOS_MIERCOLES = []
VENTAS_3D_ADULTOS_JUEVES    = []
VENTAS_3D_ADULTOS_SABADO    = []
VENTAS_3D_ADULTOS_DOMINGO   = []
VENTAS_3D_ADULTOS_VIERNES   = []
for item in Ventas3DAdultos:
    if item[12] == 'L':
        VENTAS_3D_ADULTOS_LUNES.append(item)
    elif item[14] == 'R':
        VENTAS_3D_ADULTOS_MARTES.append(item)
    elif item[16] == 'C':
        VENTAS_3D_ADULTOS_MIERCOLES.append(item)
    elif item[12] == 'J':
        VENTAS_3D_ADULTOS_JUEVES.append(item)
    elif item[12] == 'V':
        VENTAS_3D_ADULTOS_VIERNES.append(item)
    elif item[12] == 'S':
        VENTAS_3D_ADULTOS_SABADO.append(item)
    elif item[12] == 'D':
        VENTAS_3D_ADULTOS_DOMINGO.append(item)

VENTAS_3D_NIÑOS_LUNES     = []
VENTAS_3D_NIÑOS_MARTES    = []
VENTAS_3D_NIÑOS_MIERCOLES = []
VENTAS_3D_NIÑOS_JUEVES    = []
VENTAS_3D_NIÑOS_SABADO    = []
VENTAS_3D_NIÑOS_DOMINGO   = []
VENTAS_3D_NIÑOS_VIERNES   = []
for item in Ventas3DNiños:
    if item[10] == 'L':
        VENTAS_3D_NIÑOS_LUNES.append(item)
    elif item[12] == 'R':
        VENTAS_3D_NIÑOS_MARTES.append(item)
    elif item[14] == 'C':
        VENTAS_3D_NIÑOS_MIERCOLES.append(item)
    elif item[10] == 'J':
        VENTAS_3D_NIÑOS_JUEVES.append(item)
    elif item[10] == 'V':
        VENTAS_3D_NIÑOS_VIERNES.append(item)
    elif item[10] == 'S':
        VENTAS_3D_NIÑOS_SABADO.append(item)
    elif item[10] == 'D':
        VENTAS_3D_NIÑOS_DOMINGO.append(item)

listaVentas3D_Niños = [  VENTAS_3D_NIÑOS_LUNES ,   
                         VENTAS_3D_NIÑOS_MARTES   ,
                         VENTAS_3D_NIÑOS_MIERCOLES,
                         VENTAS_3D_NIÑOS_JUEVES   ,
                         VENTAS_3D_NIÑOS_VIERNES,
                         VENTAS_3D_NIÑOS_SABADO   ,
                         VENTAS_3D_NIÑOS_DOMINGO]


listaVentas3D_Adultos = [VENTAS_3D_ADULTOS_LUNES ,   
                         VENTAS_3D_ADULTOS_MARTES   ,
                         VENTAS_3D_ADULTOS_MIERCOLES,
                         VENTAS_3D_ADULTOS_JUEVES   ,
                         VENTAS_3D_ADULTOS_VIERNES ,
                         VENTAS_3D_ADULTOS_SABADO   ,
                         VENTAS_3D_ADULTOS_DOMINGO ]

Ventasxdia3D_Adultos = []
for dia in listaVentas3D_Adultos:
    listadeApoyo =[]
    for item in dia:
        listadeApoyo.append(int(item[3]))
    Ventasxdia3D_Adultos.append(sum(listadeApoyo))

Ventasxdia3D_Niños = []
for dia in listaVentas3D_Niños:
    listadeApoyo =[]
    for item in dia:
        listadeApoyo.append(int(item[3]))
    Ventasxdia3D_Niños.append(sum(listadeApoyo))
Ventas = [Ventasxdia2D_Adultos, Ventasxdia2D_Niños, Ventasxdia3D_Niños, Ventasxdia3D_Adultos]

Sum2D_Niños_Semana = sum(Ventasxdia2D_Niños[:5])
Sum2D_Niños_Finde = sum(Ventasxdia2D_Niños[5:])
Sum2D_Adultos_Semana = sum(Ventasxdia2D_Adultos[:5])
Sum2D_Adultos_Finde = sum(Ventasxdia2D_Adultos[5:])
Sum3D_Niños_Semana = sum(Ventasxdia3D_Niños[:5])
Sum3D_Niños_Finde = sum(Ventasxdia3D_Niños[5:])
Sum3D_Adultos_Semana = sum(Ventasxdia3D_Adultos[:5])
Sum3D_Adultos_Finde = sum(Ventasxdia3D_Adultos[5:])

Sumas = [[Sum2D_Niños_Semana, Sum2D_Niños_Finde],[Sum2D_Adultos_Semana, Sum2D_Adultos_Finde]],[[Sum3D_Niños_Semana,Sum3D_Niños_Finde],[Sum3D_Adultos_Semana, Sum3D_Adultos_Finde]]
dineroRecaudado2D = (Sum2D_Niños_Semana*costosCine['2D']['NIÑO']['LUN-VIE']) + (Sum2D_Niños_Finde*costosCine['2D']['NIÑO']['SAB-DOM']) + (Sum2D_Adultos_Semana*costosCine['2D']['ADULTO']['LUN-VIE']) + (Sum2D_Adultos_Finde*costosCine['2D']['ADULTO']['SAB-DOM'])
dineroRecaudado3D = (Sum3D_Niños_Semana*costosCine['3D']['NIÑO']['LUN-VIE']) + (Sum3D_Niños_Finde*costosCine['3D']['NIÑO']['SAB-DOM']) + (Sum3D_Adultos_Semana*costosCine['3D']['ADULTO']['LUN-VIE']) + (Sum3D_Adultos_Finde*costosCine['3D']['ADULTO']['SAB-DOM']) 
dineroRecaudado = dineroRecaudado2D + dineroRecaudado3D

boletasVendidas = sum(Ventasxdia2D_Adultos)+ sum(Ventasxdia2D_Niños) + sum(Ventasxdia3D_Adultos) + sum(Ventasxdia3D_Niños)
reporteCine = [boletasVendidas, dineroRecaudado]
#____________ EJERCICIO 4 ___________________
def obtenerMultiplos(numero):
    i = 1 
    multiplos = []
    int(numero)
    for j in range(0,10,1):
        multiplos.append(i*numero)
        i += 1
      
    return multiplos

def obtenerDivisores(numero):
    int(numero)
    i = numero
    divisores = []
    while i > 0:
        if numero%i == 0:
            divisores.append(i)
        i -= 1
    return divisores

def obtenerNesimoFibonacci(N):
    int(N)
    fibo = [0,1]
    for j in range(1,N):
        num_fibo = fibo[j] + fibo[j-1]
        fibo.append(num_fibo)
    return fibo[N]
funciones = [obtenerMultiplos, obtenerDivisores, obtenerNesimoFibonacci]

#____________ EJERCICIO 5 ___________________       
 
def calcularSalario(nombre, lista):
    salario = 1200000 + (1200000*0.1) + (1200000*0.05) + ((lista[0]*50000)*0.05) + + ((lista[1]*70000)*0.04) + + ((lista[2]*40000)*0.06)+ ((lista[3]*25000)*0.07) + ((lista[4]*35000)*0.05) + ((lista[5]*80000)*0.03) + ((lista[6]*95000)*0.02)
    diccionario = {'nombre':str(nombre), 'salario': salario}
    return diccionario

















    

