nombre_completo = "Sofía Londoño Toro"  
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
# __________________ LEEMOS LA BASE DE DATOS ________________________________
archivo = "estudiantes.csv"
ruta = "/Mi unidad/Semestre 6/Informática III/INFORMES/INFORME3/" + archivo
hojaEstudiantes = pd.read_csv(ruta, index_col="codigo", dtype={"codigo":str})

#_________________ PROMEDIOS POR ESTUDIANTE ____________________________________
promedio_estudiante = []
for j in range(0,500):
    media = hojaEstudiantes.iloc[j].mean(axis=0)
    promedio_estudiante += [media]
promedio_estudiante = np.array(promedio_estudiante)
promediosEstudiantes = pd.Series(data= promedio_estudiante, index= hojaEstudiantes.index)


#__________________ PROMEDIOS POR EXAMEN _________________________________________
columnas = hojaEstudiantes.columns
promedio_examen = []
for j in range(0,10):
    media = hojaEstudiantes.iloc[:, j].mean(axis=0)
    promedio_examen += [media]
promedio_examen = np.array(promedio_examen)
promediosExamenes = pd.Series(data= promedio_examen, index= hojaEstudiantes.columns)

#_____________________ ESTUDIANTE CON MEJOR PROMEDIO ______________________________
estudiante_mejor_promedio = promediosEstudiantes.idxmax()
mejorEstudiante = str(estudiante_mejor_promedio)

#_____________________ ESTUDIANTE CON PEOR PROMEDIO _______________________________
estudiante_peor_promedio = promediosEstudiantes.idxmin()
peorEstudiante = str(estudiante_peor_promedio)


#_____________________ COMPILACIÓN ANALISIS DE DATOS ______________________________
reporteEstudiantes = [promediosEstudiantes, promediosExamenes, mejorEstudiante, peorEstudiante]


#___________________________________________________________________________________


#____________________ CREACIÓN DE LA SERIE CON LOS DATOS DE VENTAS ______________________
ventas =   ["B005-22Unidades","W307-15Unidades","A011-31Unidades","P019-18Unidades","A011-20Unidades",
            "R001-20Unidades","P019-19Unidades","A001-12Unidades","A125-20Unidades","R001-31Unidades",
            "Z052-12Unidades","W307-31Unidades","Z025-42Unidades","Z052-10Unidades","A032-52Unidades",
            "B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades",
            "B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades",
            "P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades",
            "A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades",
            "Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades",
            "A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades",
            "B005-11Unidades","B001-19Unidades","B005-20Unidades","B001-19Unidades","P009-31Unidades",
            "B005-22Unidades","W307-15Unidades","Z278-30Unidades","Z025-24Unidades","P009-21Unidades",
            "Z278-30Unidades","Z025-24Unidades","Z278-11Unidades","A001-91unidades","A032-52Unidades",
            "B001-29Unidades","A125-15Unidades","A032-22Unidades","P009-25Unidades","B005-20Unidades",
            "B001-19Unidades","P009-31Unidades","B005-22Unidades","W307-15Unidades","A011-31Unidades",
            "P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades",
            "A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades",
            "Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades",
            "A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades",
            "B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades",
            "A011-31Unidades","P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades",
            "A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-12Unidades","W307-31Unidades",
            "Z025-42Unidades","Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-11Unidades",
            "A001-91unidades","A032-52Unidades","B001-29Unidades","A125-10Unidades","A011-31Unidades",
            "P019-18Unidades","A011-20Unidades","R001-20Unidades","P019-19Unidades","A001-12Unidades",
            "A125-20Unidades","R001-31Unidades","Z052-52Unidades","W307-31Unidades","Z025-42Unidades",
            "Z052-10Unidades","Z278-30Unidades","Z025-24Unidades","Z278-21Unidades","A001-31unidades",
            "A032-32Unidades","B001-22Unidades","A125-11Unidades","A032-12Unidades","P009-19Unidades",
            "B005-11Unidades","B001-19Unidades","P009-21Unidades","B005-22Unidades","W307-15Unidades",
            "A011-31Unidades","P019-18Unidades","A011-21Unidades","R001-20Unidades","P019-19Unidades",
            "A001-12Unidades","A125-20Unidades","R001-31Unidades","Z052-15Unidades","W307-31Unidades",
            "Z025-42Unidades","Z052-10Unidades","A032-22Unidades","P009-25Unidades","Z278-11Unidades",
            "A001-91unidades"]
ventas1 = sorted(ventas)

for i in range(6,12):
    ventas1[i] = ventas1[i].replace('unidades', 'Unidades')   # Ordenamos alfabeticamente la base de datos
ventas_copiaS = ventas1.copy()
ventas_copiaS = pd.Series(ventas_copiaS)

#print(ventas_copiaS[ventas_copiaS.str.contains('A011')]) # Así encuentro las posiciones de cada código
unidades = [ventas1[:12],
            ventas1[12:24],
            ventas1[24:36],
            ventas1[36:48],
            ventas1[48:60],
            ventas1[60:72],
            ventas1[72:84],
            ventas1[84:96],
            ventas1[96:108],
            ventas1[108:120],
            ventas1[120:132],
            ventas1[132:144],
            ventas1[144:156]]


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

codigos = []
for i in range(0,13):
    ref = unidadesNN[i][0][0]
    codigos += [ref]
codigos = np.array(codigos)

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
       nuevL.append(int(j))
    unidadesNNNN.append(nuevL)


unidades_totales = [] # Sumamos los items por cada articulo
for i in unidadesNNNN:
    uni = sum(i)
    unidades_totales += [uni]
unidades_totales = np.array(unidades_totales)
ventasPorProducto = pd.Series(data= unidades_totales, index= codigos)

#______________________ ANÁLISIS DE DATOS ____________________________
media = int(ventasPorProducto.mean())
mediana = int(ventasPorProducto.median())
desviacion = int(ventasPorProducto.std())
maximo = ventasPorProducto.max()
minimo = ventasPorProducto.min()
masVendido = ventasPorProducto.idxmax()
menosVendido = ventasPorProducto.idxmin()
estadisticas = [media, mediana,desviacion, maximo, minimo]
extremos = [masVendido, menosVendido]

#____________________ COMPILACIÓN ANÁLISIS ___________________________
reporteVentas = [ventasPorProducto, estadisticas, extremos]


#_____________________________________________________________________


#____________________ CREACIÓN FUNCIÓN _______________________________
x = np.arange(-3.5, 3.6, 0.01)                               
y = (x**2)*np.exp(-x**2) 


def graficaGenerica(x, y):
     #Valores numericos   
     y_derivadaOrden1 = np.diff(y)/np.diff(x)
     y_derivadaOrden2 = np.diff(y_derivadaOrden1) / np.diff(x[:-1])
     
     #Grafica
     import matplotlib.pyplot as plt
     plt.figure(figsize=(8,4))
     plt.style.use('seaborn')
     plt.subplot(1,3,1)
     plt.plot(x,y)      # y vs x
     plt.title('F(x)')
     plt.xlim(-3, 3)
     plt.ylim(-2,2)
     plt.grid(True)
     plt.subplot(1,3,2)
     plt.plot(x[:-1],y_derivadaOrden1) # y' vs x
     plt.title("F'(x)")
     plt.xlim(-3, 3)
     plt.ylim(-2,2)
     plt.grid(True)      
     plt.subplot(1,3,3)
     plt.plot(x[:-2], y_derivadaOrden2)      # y'' vs x
     plt.title("F''(x)")
     plt.xlim(-3, 3)
     plt.ylim(-2,2.2)
     plt.grid(True)
     plt.legend()
     plt.show()



