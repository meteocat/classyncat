def classyncat(tipus_sfc: dict, tipus_500: dict) -> dict:
    """This subroutine is the main core of the synoptic classification in which
    is based in:
    Miró et al(2020): Daily atmospheric circulation patterns for Catalonia
    (northeast Iberian Peninsula) using a modified version of Jenkinson and
    Collison method.
    Respect the original we've made some changes:
    TIP11 (Dana in the SW) was assimilated to TIP09 (SW advection)
    TIP13 (Thermal Low) and TIP14 (Barometric swamp) were fussioned.
    TIP16 (Anticiclo Termic) ha estat assimilat al anticiclo normal (TIP13)    

    Types:
    TIP01: Adveccio Oest
    TIP02: Adveccio del Oest Anticiclonica
    TIP03: Adveccio del NW
    TIP04: Adveccio del N
    TIP05: Adveccio del NE
    TIP06: Adveccio del E
    TIP07: Adveccio del E amb gota freda
    TIP08: Adveccio del S
    TIP09: Adveccio del SW
    TIP10: Solc
    TIP11: Ciclo
    TIP12: Indefinit o baixa superficial
    TIP13: Anticiclo

    Args:
        tipus_sfc (dict): Corresponding types calcultad with surface pressure
        tipus_500 (dict): Corresponding types calcultad with 500mb geopotential

    Returns:
        dict: classificacio obtinguda amb la combinació de les dues 
        classificacions.
    """

    tipus = 'None'
    classificacio = {}

    for dia in tipus_sfc.keys():
        tipus1 = tipus_sfc[dia]
        tipus2 = tipus_500[dia]
        # Slicing for the types in sfc and 500 we construct the new
        # classification
        if (tipus1 == 'A'):
            if (tipus2[0] == 'C'):
                if (tipus2 == 'C'):
                    tipus = 'TIP13'
                elif (tipus2 == 'CSW' or tipus2 == 'CW' or tipus2 == 'CNW'):
                    tipus = 'TIP02'
                else:
                    tipus = 'TIP13'
            elif (tipus2[0] == 'A'):
                if (tipus2 == 'A'):
                    tipus = 'TIP13'
                elif (tipus2 == 'ASW' or tipus2 == 'AW' or tipus2 == 'ANW'):
                    tipus = 'TIP02'
                else:
                    tipus = 'TIP13'
            else:
                if (tipus2 == 'SW' or tipus2 == 'W' or tipus2 == 'NW'):
                    tipus = 'TIP02'
                else:
                    tipus = 'TIP13'

        elif (tipus1 == 'AE' or tipus1 == 'ASE'):
            if (tipus2[0] == 'C'):
                tipus = 'TIP07'
            else:
                tipus = 'TIP06'
        elif (tipus1 == 'AS'):
            tipus = 'TIP08'
        elif (tipus1 == 'ASW'):
            tipus = 'TIP09'
        elif (tipus1 == 'AW'):
            tipus = 'TIP02'
        elif (tipus1 == 'ANW'):
            tipus = 'TIP03'
        elif (tipus1 == 'AN'):
            tipus = 'TIP04'
        elif (tipus1 == 'ANE'):
            tipus = 'TIP05'

        elif (tipus1 == 'C'):
            if (tipus2[0] == 'C'):
                tipus = 'TIP11'
            elif (tipus2[0] == 'A'):
                if (tipus2 == 'AW' or tipus2 == 'ASW' or tipus2 == 'AE' or
                   tipus2 == 'ASE' or tipus2 == "A"):
                    tipus = 'TIP12'
                else:
                    tipus = 'TIP11'
            elif (tipus2 == 'U'):
                tipus = 'TIP12'
            else:
                if (tipus2 == 'W' or tipus2 == 'SW' or
                   tipus2 == 'E' or tipus2 == 'SE'):
                    tipus = 'TIP12'
                else:
                    tipus = 'TIP11'

        elif (tipus1 == 'CE' or tipus1 == 'CSE'):
            if (tipus2[0] == 'C'):
                tipus = 'TIP07'
            else:
                tipus = 'TIP06'
        elif (tipus1 == 'CS'):
            tipus = 'TIP08'
        elif (tipus1 == 'CSW'):
            tipus = 'TIP09'
        elif (tipus1 == 'CW'):
            if (tipus2[0] == 'C'):
                tipus = 'TIP10'
            else:
                tipus = 'TIP01'
        elif (tipus1 == 'CNW'):
            tipus = 'TIP03'
        elif (tipus1 == 'CN'):
            tipus = 'TIP04'
        elif (tipus1 == 'CNE'):
            tipus = 'TIP05'
        elif (tipus1 == 'E' or tipus1 == 'SE'):
            if (tipus2[0] == 'C'):
                tipus = 'TIP07'
            else:
                tipus = 'TIP06'
        elif (tipus1 == 'S'):
            tipus = 'TIP08'
        elif (tipus1 == 'SW'):
            tipus = 'TIP09'
        elif (tipus1 == 'W'):
            tipus = 'TIP01'
        elif (tipus1 == 'NW'):
            tipus = 'TIP03'
        elif (tipus1 == 'N'):
            tipus = 'TIP04'
        elif (tipus1 == 'NE'):
            tipus = 'TIP05'
        elif (tipus1 == 'U'):
            if (tipus2[0] == 'C'):
                if (tipus2 == 'CS' or tipus2 == 'CSW' or tipus2 == 'CSE'):
                    tipus = 'TIP09'
                else:
                    tipus = 'TIP10'
            else:
                tipus = 'TIP12'

        classificacio[dia] = tipus

    return classificacio
