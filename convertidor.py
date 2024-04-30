def contarLetras(text):
    contador = 0
    for i in text:
        contador += 1
    return contador


def base2_a_base2(numero):
    res=0
    exponentee=0
    while numero>0:
        nuevo= numero % 10
        res += nuevo * (2 ** exponentee )
        numero //= 10
        exponentee += 1
    return res
#base2_a_base2(1010))        


def base2_a_base3(numero):
    res = 0
    exponentee = 0
    base3 = 0
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
    
    multiplier = 1
    while res > 0:
        todo = res % 3
        base3 += todo * multiplier
        res //= 3
        multiplier *= 10
    
    return base3
#base2_a_base3(1010))


def base2_a_base4(numero):
    res = 0
    exponentee = 0
    base4 = 0
    
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
    
    multiplier = 1
    while res > 0:
        todo = res % 4
        base4 += todo * multiplier
        res //= 4
        multiplier *= 10
    
    return base4
#base2_a_base4(1010))



def base2_a_base5(numero):
    res = 0
    exponentee = 0
    base5 = 0
    
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
    
    multiplier = 1
    while res > 0:
        todo = res % 5
        base5 += todo * multiplier
        res //= 5
        multiplier *= 10
    
    return base5
#base2_a_base5(1010))


def base2_a_base6(numero):
    res = 0
    exponentee = 0
    base6 = 0
    
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
    
    multiplier = 1
    while res > 0:
        todo = res % 6
        base6 += todo * multiplier
        res //= 6
        multiplier *= 10
    
    return base6
#base2_a_base6(1010))

def base2_a_base7(numero):
    res = 0
    exponentee = 0
    base7 = 0
    
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
   
    multiplier = 1
    while res > 0:
        todo = res % 7
        base7 += todo * multiplier
        res //= 7
        multiplier *= 10
    
    return base7
#base2_a_base7(1010))

def base2_a_base8(numero):
    res = 0
    exponentee = 0
    base8 = 0
    
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
    
    multiplier = 1
    while res > 0:
        todo = res % 8
        base8 += todo * multiplier
        res //= 8
        multiplier *= 10
    
    return base8
#base2_a_base8(1010))


def base2_a_base9(numero):
    res = 0
    exponentee = 0
    base9 = 0
    
    
    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1
    
   
    multiplier = 1
    while res > 0:
        todo = res % 9
        base9 += todo * multiplier
        res //= 9
        multiplier *= 10
    
    return base9
#base2_a_base9(1010))

def base2_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base2_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base2_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base2_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base2_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base2_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base2_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (2 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16


################################################################################################################################
def base3_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base3_to_base2(10))


def base3_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base3_to_base3(10))

def base3_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base3_to_base4(10))

def base3_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
# base3_to_base5(10))

def base3_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base3_to_base6(10))

def base3_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base3_to_base7(10))

def base3_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base3_to_base8(10))

def base3_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (3 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base3_to_base9(10))

def base3_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base3_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base3_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base3_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base3_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base3_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base3_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (3 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16


#===================================================================================================================================0
def base4_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base4_to_base2(30))

def base4_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base4_to_base3(30))

def base4_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base4_to_base4(30))

def base4_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
# base4_to_base5(30))

def base4_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base4_to_base6(30))

def base4_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base4_to_base7(30))

def base4_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base4_to_base8(30))

def base4_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (4 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base4_to_base9(30))

def base4_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base4_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base4_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base4_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base4_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base4_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base4_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (4 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16


#======================================================================================================================================0
#3
def base5_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base5_to_base2(30))

def base5_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base5_to_base3(30))

def base5_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base5_to_base4(30))

def base5_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
# base5_to_base5(30))

def base5_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base5_to_base6(30))

def base5_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base5_to_base7(30))

def base5_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base5_to_base8(30))

def base5_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (5 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base5_to_base9(30))

def base5_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base5_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base5_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base5_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base5_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base5_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base5_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (5 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16



#======================================================================================================================================0
#4
def base6_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base6_to_base2(30))

def base6_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base6_to_base3(30))

def base6_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base6_to_base4(30))

def base6_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
# base6_to_base5(30))

def base6_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base6_to_base6(30))

def base6_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base6_to_base7(30))

def base6_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base6_to_base8(30))

def base6_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (6 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base6_to_base9(30))

def base6_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base6_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base6_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base6_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base6_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base6_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base6_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (6 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16



#======================================================================================================================================0
#5
def base7_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base7_to_base2(30))

def base7_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base7_to_base3(30))

def base7_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base7_to_base4(30))

def base7_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
#base7_to_base5(30))

def base7_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base7_to_base6(30))

def base7_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base7_to_base7(30))

def base7_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base7_to_base8(30))

def base7_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (7 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base7_to_base9(30))

def base7_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base7_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base7_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base7_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base7_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base7_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base7_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (7 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16


#======================================================================================================================================0
#6

def base8_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base8_to_base2(30))

def base8_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base8_to_base3(30))

def base8_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base8_to_base4(30))

def base8_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
#base8_to_base5(30))

def base8_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base8_to_base6(30))

def base8_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base8_to_base7(30))

def base8_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base8_to_base8(30))

def base8_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (8 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base8_to_base9(30))

def base8_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base8_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base8_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base8_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base8_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base8_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base8_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (8 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16



#======================================================================================================================================0

#7
def base9_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base9_to_base2(30))

def base9_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base9_to_base3(30))

def base9_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base9_to_base4(30))

def base9_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
#base9_to_base5(30))

def base9_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base9_to_base6(30))

def base9_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base9_to_base7(30))

def base9_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base9_to_base8(30))

def base9_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (9 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base9_to_base9(30))

def base9_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base9_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base9_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base9_a_base13(numero):
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base9_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base9_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base9_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (9 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16


#======================================================================================================================================0

#8
def base10_a_base2(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 2
        binario += todo * valor
        decimal //= 2
        valor *= 10
    
    return binario
# base10_to_base2(30))

def base10_a_base3(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 3
        binario += todo * valor
        decimal //= 3
        valor *= 10
    
    return binario
# base10_to_base3(30))

def base10_a_base4(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 4
        binario += todo * valor
        decimal //= 4
        valor *= 10
    
    return binario
# base10_to_base4(30))

def base10_a_base5(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 5
        binario += todo * valor
        decimal //= 5
        valor *= 10
    
    return binario
#base10_to_base5(30))

def base10_a_base6(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 6
        binario += todo * valor
        decimal //= 6
        valor *= 10
    
    return binario
# base10_to_base6(30))

def base10_a_base7(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 7
        binario += todo * valor
        decimal //= 7
        valor *= 10
    
    return binario
# base10_to_base7(30))

def base10_a_base8(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 8
        binario += todo * valor
        decimal //= 8
        valor *= 10
    
    return binario
# base10_to_base8(30))

def base10_a_base9(numero):
    decimal = 0
    exponente = 0
    
    while numero > 0:
        digitos = numero % 10
        decimal += digitos * (10 ** exponente)
        numero //= 10
        exponente += 1
    
    binario = 0
    valor = 1
    while decimal > 0:
        todo = decimal % 9
        binario += todo * valor
        decimal //= 9
        valor *= 10
    
    return binario
# base10_to_base9(30))

def base10_a_base10(numero):
    res = 0
    exponentee = 0
    base10 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 10
        base10 = diles[todo] + base10
        res //= 10

    return base10

def base10_a_base11(numero):
    res = 0
    exponentee = 0
    base11 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 11
        base11 = diles[todo] + base11
        res //= 11

    return base11





def base10_a_base12(numero):
    res = 0
    exponentee = 0
    base12 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 12
        base12 = diles[todo] + base12
        res //= 12

    return base12


def base10_a_base13(numero):
    if numero == 'A':
        return 'A'
    elif numero == 'B':
        return 'B'
    elif numero == 'C':
        return 'C'
    elif numero == 'D':
        return '10'
    res = 0
    exponentee = 0
    base13 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 13
        base13 = diles[todo] + base13
        res //= 13

    return base13


def base10_a_base14(numero):
    res = 0
    exponentee = 0
    base14 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 14
        base14 = diles[todo] + base14
        res //= 14

    return base14


def base10_a_base15(numero):
    res = 0
    exponentee = 0
    base15 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 15
        base15 = diles[todo] + base15
        res //= 15

    return base15

def base10_a_base16(numero):
    res = 0
    exponentee = 0
    base16 = ""

    
    diles = "0123456789ABCDEF"

    while numero > 0:
        nuevo = numero % 10
        res += nuevo * (10 ** exponentee)
        numero //= 10
        exponentee += 1

    while res > 0:
        todo = res % 16
        base16 = diles[todo] + base16
        res //= 16

    return base16


#======================================================================================================================================0
#=======================================================================================0
def base11_a_base2(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base2(res)
    return res


def base11_a_base3(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base3(res)
    return res


def base11_a_base4(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base4(res)
    return res

def base11_a_base5(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base5(res)
    return res

def base11_a_base6(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base6(res)
    return res


def base11_a_base7(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base7(res)
    return res


def base11_a_base8(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base8(res)
    return res


def base11_a_base9(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res

def base11_a_base10(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    return res

def base11_a_base11(numero):
    return numero


def base11_a_base12(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base12(res)
    return res


def base11_a_base13(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base13(res)
    return res

def base11_a_base14(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base14(res)
    return res

def base11_a_base15(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base15(res)
    return res

def base11_a_base16(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(11 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base16(res)
    return res
#=========================================================================================================================================0
#=======================================================================================0
def base12_a_base2(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base2(res)
    return res


def base12_a_base3(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base3(res)
    return res


def base12_a_base4(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base4(res)
    return res

def base12_a_base5(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base5(res)
    return res

def base12_a_base6(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base6(res)
    return res


def base12_a_base7(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base7(res)
    return res


def base12_a_base8(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base8(res)
    return res


def base12_a_base9(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res

def base12_a_base10(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    return res

def base12_a_base11(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base11(res)
    return res


def base12_a_base12(numero):
    return numero


def base12_a_base13(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base13(res)
    return res

def base12_a_base14(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base14(res)
    return res

def base12_a_base15(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base15(res)
    return res

def base12_a_base16(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(12 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base16(res)
    return res

#====================================================================================================================================00
#=======================================================================================0
def base13_a_base2(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base2(res)
    return res


def base13_a_base3(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base3(res)
    return res

def base13_a_base4(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base4(res)
    return res

def base13_a_base5(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base5(res)
    return res

def base13_a_base6(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base6(res)
    return res


def base13_a_base7(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base7(res)
    return res


def base13_a_base8(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base8(res)
    return res


def base13_a_base9(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res

def base13_a_base10(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    return res

def base13_a_base11(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res


def base13_a_base12(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base12(res)
    return res


def base13_a_base13(numero):
    return numero

def base13_a_base14(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base14(res)
    return res

def base13_a_base15(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base15(res)
    return res

def base13_a_base16(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito = 12
        else:
            digito = int(numero[indice])
        
        res += digito *(13 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base16(res)
    return res


#=========================================================================================00
#=======================================================================================0
def base14_a_base2(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base2(res)
    return res


def base14_a_base3(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base3(res)
    return res


def base14_a_base4(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base4(res)
    return res

def base14_a_base5(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base5(res)
    return res

def base14_a_base6(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base6(res)
    return res


def base14_a_base7(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base7(res)
    return res


def base14_a_base8(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base8(res)
    return res


def base14_a_base9(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res

def base14_a_base10(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    return res

def base14_a_base11(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base11(res)
    return res


def base14_a_base12(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base12(res)
    return res


def base14_a_base13(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base13(res)
    return res

def base14_a_base14(numero):
    return numero

def base14_a_base15(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base15(res)
    return res

def base14_a_base16(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(14 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base16(res)
    return res

#=======================================================================================0
def base15_a_base2(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base2(res)
    return res


def base15_a_base3(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base3(res)
    return res


def base15_a_base4(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base4(res)
    return res

def base15_a_base5(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base5(res)
    return res

def base15_a_base6(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base6(res)
    return res


def base15_a_base7(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base7(res)
    return res


def base15_a_base8(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base8(res)
    return res


def base15_a_base9(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res

def base15_a_base10(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    return res

def base15_a_base11(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base11(res)
    return res


def base15_a_base12(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base12(res)
    return res


def base15_a_base13(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base13(res)
    return res

def base15_a_base14(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base14(res)
    return res

def base15_a_base15(numero):
    return numero

def base15_a_base16(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        else:
            digito = int(numero[indice])
        
        res += digito *(15 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base16(res)
    return res

#============================================================================================0

def base16_a_base2(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base2(res)
    return res


def base16_a_base3(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base3(res)
    return res

def base16_a_base4(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base4(res)
    return res


def base16_a_base5(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base5(res)
    return res

def base16_a_base6(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base6(res)
    return res

def base16_a_base7(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base7(res)
    return res


def base16_a_base8(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base8(res)
    return res


def base16_a_base9(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base9(res)
    return res

#================================================================================0
def base16_a_base10(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    return res
#================================================================000


def base16_a_base11(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base11(res)
    return res

def base16_a_base12(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base12(res)
    return res

def base16_a_base13(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base13(res)
    return res


def base16_a_base14(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base14(res)
    return res

def base16_a_base15(numero):
    res = 0
    exponente = 0
    indice = contarLetras(numero) -1
    while (indice > -1):
        if (numero[indice] == "A"):
            digito = 10
        elif (numero[indice] == "B"):
            digito = 11
        elif (numero[indice] == "C"):
            digito == 12
        elif (numero[indice] == "D"):
            digito = 13
        elif (numero[indice] == "E"):
            digito = 14
        elif (numero[indice] == "F"):
            digito = 15
        else:
            digito = int(numero[indice])
        
        res += digito *(16 **exponente)
        exponente += 1
        indice -= 1
    res = base10_a_base15(res)
    return res


def base16_a_base16(numero):
    return numero
