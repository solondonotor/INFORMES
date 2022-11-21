'''
Este módulo contiene funciones que reciben un número en decimal y lo convierten a binario,
octal o hexadecimal respectivamente, mediante las siguientes funciones:
            convertirABinario     => recibe string (cadena_decimal), retorna string (cadena_binario)
            convertirAOctal       => recibe string (cadena_decimal), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_decimal), retorna string (cadena_hexadecimal)
'''

from numpy import log10

def  convertirABinario(cadena_decimal:str):
    numero_decimal = int(cadena_decimal)
    lista_binario = []
    while numero_decimal > 0:
        residuo = numero_decimal % 2
        numero_decimal = numero_decimal// 2
        lista_binario += [residuo]
    cadena_binario = ''
    for i in reversed(lista_binario):
        cadena_binario += str(i)
    return cadena_binario

def convertirAOctal(cadena_decimal:str):
    numero_decimal = int(cadena_decimal)
    lista_octal = []
    while numero_decimal > 0:
        residuo = numero_decimal % 8
        numero_decimal = numero_decimal// 8
        lista_octal += [residuo]
    cadena_octal = ''
    for i in reversed(lista_octal):
        cadena_octal += str(i)
    return cadena_octal

def convertirAHexadecimal(cadena_decimal:str):
    numero_decimal = int(cadena_decimal)
    lista_hexadecimal = []
    while numero_decimal > 0:
        residuo = numero_decimal % 16
        if residuo == 10:
            residuo = 'A'
        if residuo == 11:
            residuo = 'B' 
        if residuo == 12:
            residuo = 'C'
        if residuo == 13:
            residuo = 'D'
        if residuo == 14:
            residuo = 'E'
        if residuo == 15:
            residuo = 'F'
        numero_decimal = numero_decimal// 16
        lista_hexadecimal += [residuo]
    cadena_hexadecimal = ''
    for i in reversed(lista_hexadecimal):
        cadena_hexadecimal += str(i)
    return cadena_hexadecimal






if __name__ == '__main__': #Prueba las funciones
    print(convertirABinario('2567'))
    print(convertirAOctal('8'))
    print(convertirAHexadecimal('123456890'))
