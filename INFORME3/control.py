import Decimal_, binario, octal, hexadecimal
i = 1
while i > 0:
    print('Bienvendio al conversor de números')
    print('-' * 100)
    print('Seleccione en que sistema se encuentra el número a ingresar:')
    seleccion_entrada = int(input('1.Decimal 2.Octal 3.Binario 4.Hexadecimal '))
    print('Seleccione a que sistema desea convertir su número:')
    seleccion_conversion = str(input('A. Decimal   B. Binario   C. Octal   D. Hexadecimal '))

    if seleccion_entrada == 1:
        numero = str(input('Ingrese el número en Decimal: '))
        if seleccion_conversion == 'A':
            numero_conversor = numero
        elif seleccion_conversion == 'B':
            numero_conversor =  Decimal_.convertirABinario(numero)
        elif seleccion_conversion == 'C':
            numero_conversor =  Decimal_.convertirAOctal(numero)
        elif seleccion_conversion == 'D':
            numero_conversor = Decimal_.convertirAHexadecimal(numero)
        else:
            print('Caracter no válido')
            break

    elif seleccion_entrada == 2:
        numero = str(input('Ingrese el número en Octal: '))
        if seleccion_conversion == 'A':
            numero_conversor = octal.convertirADecimal(numero)
        elif seleccion_conversion == 'B':
            numero_conversor =  octal.convertirABinario(numero)
        elif seleccion_conversion == 'C':
            numero_conversor =  numero
        elif seleccion_conversion == 'D':
            numero_conversor = octal.convertirAHexadecimal(numero)
        else:
            print('Caracter no válido')
            break

    elif seleccion_entrada == 3:
        numero = str(input('Ingrese el número en Binario: '))
        if seleccion_conversion == 'A':
            numero_conversor = binario.convertirADecimal(numero)
        elif seleccion_conversion == 'B':
            numero_conversor =  numero
        elif seleccion_conversion == 'C':
            numero_conversor =  binario.convertirAOctal(numero)
        elif seleccion_conversion == 'D':
            numero_conversor = binario.convertirAHexadecimal(numero)
        else:
            print('Caracter no válido')
            break

    elif seleccion_entrada == 4:
        numero = str(input('Ingrese el número en Hexadecimal: '))
        if seleccion_conversion == 'A':
            numero_conversor = hexadecimal.convertirADecimal(numero)
        elif seleccion_conversion == 'B':
            numero_conversor =  hexadecimal.convertirABinario(numero)
        elif seleccion_conversion == 'C':
            numero_conversor =  hexadecimal.convertirAOctal(numero)
        elif seleccion_conversion == 'D':
            numero_conversor = numero
        else:
            print('Caracter no válido')
            break

    else:
        print('Caracter no válido')
        break
    print('La conversión es: ', numero_conversor)
    break


