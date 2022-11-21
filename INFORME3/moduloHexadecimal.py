''' 
Este módulo contiene funciones que reciben un número en sistema hexadecimal y retornas sus respectivas
conversiones a decimal, binario y octal, mediante las siguientes funciones:
            convertirABinario => recibe string (cadena_hexadecimal), retorna string (cadena_binario)
            convertirADecimal => recibe string (cadena_hexadecimal), retorna string (cadena_decimal)
            convertirAOctal   => recibe string (cadena_hexadecimal), retorna string (cadena_Octal)
'''
import Decimal_

def convertirADecimal(cadena_hexadecimal:str):
    lista_hexadecimal = list(cadena_hexadecimal)
    lista_hexadecimal = reversed(lista_hexadecimal)
    J = 0
    cadena_decimal = 0
    for i in lista_hexadecimal:
        if i == 'A':
            numero_i = 10
        elif i == 'B':
            numero_i = 11
        elif i == 'C':
            numero_i = 12
        elif i == 'D':
            numero_i = 13
        elif i == 'E':
            numero_i = 14
        elif i == 'F':
            numero_i = 15
        else:
            numero_i = int(i)
        cadena_decimal += numero_i*(16**J)
        J += 1
    return cadena_decimal

def convertirABinario(cadena_hexadecimal:str):
    numero_decimal = convertirADecimal(cadena_hexadecimal)
    cadena_binario = Decimal_.convertirABinario(numero_decimal)
    return cadena_binario

def convertirAOctal(cadena_hexadecimal:str):
    numero_decimal = convertirADecimal(cadena_hexadecimal)
    cadena_Octal = Decimal_.convertirAOctal(numero_decimal)
    return cadena_Octal

if __name__ == '__main__': #Prueba las funciones
    print(convertirADecimal('F12A4'))
    print(convertirAOctal('A'))