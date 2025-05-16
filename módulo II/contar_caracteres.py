def contar_caracteres(string):
    
    contador = {}

    
    for item in string:
        if item in contador:
            contador[item] += 1
        else:
            contador[item] = 1

    return contador


entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
