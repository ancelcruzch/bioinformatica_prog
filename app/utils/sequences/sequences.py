def convertir_adn_a_arn(adn):
    # Lógica de conversión de ADN a ARN
    arn = adn.replace('T', 'U')
    return arn

def tipo_secuencia(secuencia):
    # Convertir la secuencia a mayúsculas para evitar problemas con mayúsculas/minúsculas
    secuencia = secuencia.upper()

    # Definir conjuntos de caracteres para ADN, ARN y proteínas
    caracteres_adn = set("ACGT")
    caracteres_arn = set("ACGU")
    caracteres_proteina = set("ACDEFGHIKLMNPQRSTVWY")

    # Verificar si la secuencia es ADN
    if all(caracter in caracteres_adn for caracter in secuencia):
        return "ADN"
    
    # Verificar si la secuencia es ARN
    elif all(caracter in caracteres_arn for caracter in secuencia):
        return "ARN"
    
    # Verificar si la secuencia es una proteína
    elif all(caracter in caracteres_proteina for caracter in secuencia):
        return "PROTEINA"
    
    # Si no cumple con ninguno de los anteriores, es otro tipo de secuencia
    else:
        return "OTRO"