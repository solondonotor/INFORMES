'''
Este módulo contienes funciones que reciben un número en sistema binario y lo convierten respectivamente
a decimal, octal o hexadecimal, mediante las siguientes funciones:
            convertirADecimal     => recibe string (cadena_binario), retorna string (cadena_decimal)
            convertirAOctal       => recibe string (cadena_binario), retorna string (cadena_octal)
            convertirAHexadecimal => recibe string (cadena_binario), retorna string (cadena_hexadecimal)

'''
import Decimal_

def convertirADecimal(cadena_binario: str):
    lista_binario = list(cadena_binario)
    lista_binario = reversed(lista_binario)
    J = 0
    cadena_decimal = 0
    for i in lista_binario:
        numero_i = int(i)
        cadena_decimal += numero_i*(2**J)
        J += 1
    return cadena_decimal

def convertirAOctal(cadena_binario:str):
    decimal1 = convertirADecimal(cadena_binario)
    cadena_octal = Decimal_.convertirAOctal(decimal1)
    return cadena_octal

def convertirAHexadecimal(cadena_binario : str):
    decimal1 = convertirADecimal(cadena_binario)
    cadena_hexadecimal = Decimal_.convertirAHexadecimal(decimal1)
    return cadena_hexadecimal

if __name__ == '__main__': #Prueba las funciones
    print(convertirADecimal('1010'))
    print(convertirAHexadecimal('1010'))
    
