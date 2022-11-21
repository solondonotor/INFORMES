'''
Este módulo contiene funciones que reciben un número en sistema octal y lo convierten respectivamente
en binario, decimal o hexadecimal, mediante las siguientes funciones:
            convertirABinario     => recibe string (cadena_octal), retorna string (cadena_binario)
            convertirADecimal     => recibe string (cadena_octal), retorna string (cadena_decimal)
            convertirAHexadecimal => recibe string (cadena_octal), retorna string (cadena_hexadecimal)

'''
import Decimal_

def convertirADecimal(cadena_octal: str):
    lista_octal = list(cadena_octal)
    lista_octal = reversed(lista_octal)
    J = 0
    cadena_decimal = 0
    for i in lista_octal:
        numero_i = int(i)
        cadena_decimal += numero_i*(8**J)
        J += 1
    return cadena_decimal

def convertirABinario(cadena_octal:str):
    conversion_decimal = convertirADecimal(cadena_octal)
    cadena_binario = Decimal_.convertirABinario(conversion_decimal)
    return cadena_binario

def convertirAHexadecimal(cadena_octal:str):
    conversion_decimal = convertirADecimal(cadena_octal)
    cadena_hexadecimal = Decimal_.convertirAHexadecimal(conversion_decimal)
    return cadena_hexadecimal


if __name__ == '__main__': #Prueba las funciones
    print(convertirAHexadecimal('12'))
    