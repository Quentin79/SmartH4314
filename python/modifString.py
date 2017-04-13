def modifierString (strInitiale):
    strFinal = strInitiale.lower()
    strFinal = strFinal.replace(' ', '')
    strFinal = strFinal.replace(',', '')
    strFinal = strFinal.replace(';', '')
    strFinal = strFinal.replace('-', '')
    strFinal = strFinal.replace('_', '')
    strFinal = strFinal.replace('\'', '')
    strFinal = strFinal.replace('/', '')
    strFinal = strFinal.replace('\\', '')
    strFinal = strFinal.replace('!', '')
    strFinal = strFinal.replace('?', '')
    strFinal = strFinal.replace('"', '')
    strFinal = strFinal.replace('...', '')
    strFinal = strFinal.replace('<', '')
    strFinal = strFinal.replace('>', '')


    strFinal = strFinal.replace('à', 'a')
    strFinal = strFinal.replace('â', 'a')

    strFinal = strFinal.replace('ç', 'c')

    strFinal = strFinal.replace('é', 'e')
    strFinal = strFinal.replace('è', 'e')
    strFinal = strFinal.replace('ê', 'e')
    strFinal = strFinal.replace('ë', 'e')


    strFinal = strFinal.replace('î', 'i')
    strFinal = strFinal.replace('ï', 'i')

    strFinal = strFinal.replace('ô', 'o')

    strFinal = strFinal.replace('û', 'u')
    strFinal = strFinal.replace('ü', 'u')
    strFinal = strFinal.replace('ù', 'u')

    return strFinal

