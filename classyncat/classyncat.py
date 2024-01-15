'''
Tipus simplificats:

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
'''


def classyncat(tipus_sfc, tipus_500):

    # This subroutine is the main core of the synoptic classification in which
    # from the previously calculated classifications of J&C in sfc and 500 mb 
    # we define a type related to the Martin Vide (2014) manual classification. 
    # Respect the original we've made some changes:
    # TIP11 (Dana in the SW) was assimilated to TIP09 (SW advection)
    # TIP13 (Thermal Low) and TIP14 (Barometric swamp) were fussioned.
    # TIP16 (Anticiclo Termic) ha estat assimilat al anticiclo normal (TIP13)
    # The original types were reduced to 13.

    tipus = 'kk'
    classificacio = {}

    for dia in tipus_sfc.keys():
        tipus1 = tipus_sfc[dia]
        tipus2 = tipus_500[dia]
        # Cas Anticiclo en superficie
        if (tipus1 == 'A'):
            if (tipus2[0] == 'C'):
                if (tipus2 == 'C'):
                    # Seria Anticiclo termic pero ho assimilarem a TIP13
                    tipus = 'TIP13'
                elif (tipus2 == 'CSW' or tipus2 == 'CW' or tipus2 == 'CNW'):
                    # Adveccio del W anticiclonica
                    tipus = 'TIP02'
                else:
                    # Anticiclo
                    tipus = 'TIP13'
            elif (tipus2[0] == 'A'):
                if (tipus2 == 'A'):
                    # Anticiclo
                    tipus = 'TIP13'
                elif (tipus2 == 'ASW' or tipus2 == 'AW' or tipus2 == 'ANW'):
                    # Adveccio del W anticiclonica
                    tipus = 'TIP02'
                else:
                    # Anticiclo
                    tipus = 'TIP13'
            else:
                if (tipus2 == 'SW' or tipus2 == 'W' or tipus2 == 'NW'):
                    # Adveccio del W anticiclonica
                    tipus = 'TIP02'
                else:
                    # Anticiclo
                    tipus = 'TIP13'

        # Cas anticiclo del E o be del SE (AE o ASE)        

        elif (tipus1 == 'AE' or tipus1 == 'ASE'):
            if (tipus2[0] == 'C'):
                # Adveccio del E amb gota freda
                tipus = 'TIP07'
            else:
                # Adveccio del E
                tipus = 'TIP06'

        # Cas anticiclo del S (AS)

        elif (tipus1 == 'AS'):
            # Adveccio del S
            tipus = 'TIP08'

        # Cas anticiclo del SW (ASW)

        elif (tipus1 == 'ASW'):
            # Adveccio del SW
            tipus = 'TIP09'

        # Cas anticiclo del W (AW)

        elif (tipus1 == 'AW'):
            # Adveccio del W
            tipus = 'TIP02'

        # Cas anticiclo del NW

        elif (tipus1 == 'ANW'):
            # Adveccio del NW
            tipus = 'TIP03'

        # Cas anticiclo del N

        elif (tipus1 == 'AN'):
            # Adveccio del N
            tipus = 'TIP04'

        # Cas anticiclo del NE

        elif (tipus1 == 'ANE'):
            # Adveccio del NE
            tipus = 'TIP05'

        # Cas ciclo (C)

        elif (tipus1 == 'C'):
            if (tipus2[0] == 'C'):
                # Ciclo
                tipus = 'TIP11'
            elif (tipus2[0] == 'A'):
                if (tipus2 == 'AW' or tipus2 == 'ASW' or tipus2 == 'AE' or
                   tipus2 == 'ASE' or tipus2 == "A"):
                    # Tipus indeterminat: panta barometric o baixa superficial
                    tipus = 'TIP12'
                else:
                    # Ciclo
                    tipus = 'TIP11'
            elif (tipus2 == 'U'):
                # Tipus indeterminat: panta barometric o baixa superficial
                tipus = 'TIP12'
            else:
                if (tipus2 == 'W' or tipus2 == 'SW' or
                   tipus2 == 'E' or tipus2 == 'SE'):
                    # Tipus indeterminat: panta barometric o baixa superficial
                    tipus = 'TIP12'
                else:
                    # Ciclo
                    tipus = 'TIP11'

        # Cas ciclo del Est i del Sud-Est (CE i CSE)

        elif (tipus1 == 'CE' or tipus1 == 'CSE'):
            if (tipus2[0] == 'C'):
                # Adveccio del E amb gota freda
                tipus = 'TIP07'
            else:
                # Adveccio del E
                tipus = 'TIP06'

        # Cas ciclo del Sud (CS)

        elif (tipus1 == 'CS'):
            # Adveccion del S
            tipus = 'TIP08'

        # Cas ciclo del SE (CSW)

        elif (tipus1 == 'CSW'):
            # Adveccio del SW
            tipus = 'TIP09'

        # Cas ciclo del W (CW)

        elif (tipus1 == 'CW'):
            if (tipus2[0] == 'C'):
                # Solc
                tipus = 'TIP10'
            else:
                # Adveccio W
                tipus = 'TIP01'

        # Cas cilo del NW (CNW)  

        elif (tipus1 == 'CNW'):
            # Adveccio del NW
            tipus = 'TIP03'

        # Cas ciclo del N

        elif (tipus1 == 'CN'):
            # Adveccio N
            tipus = 'TIP04'

        # Cas ciclo del N

        elif (tipus1 == 'CNE'):
            # Adveccio NE
            tipus = 'TIP05'

        # Cas advectiu del E i del SE

        elif (tipus1 == 'E' or tipus1 == 'SE'):
            if (tipus2[0] == 'C'):
                # Adveccio de E amb gota freda
                tipus = 'TIP07'
            else:
                # Adveccio de E
                tipus = 'TIP06'

        # Cas advectiu del S

        elif (tipus1 == 'S'):
            tipus = 'TIP08'

        # Cas advectiu del SW

        elif (tipus1 == 'SW'):
            tipus = 'TIP09'

        # Cas advectiu del W

        elif (tipus1 == 'W'):
            tipus = 'TIP01'

        # Cas advectiu del NW

        elif (tipus1 == 'NW'):
            tipus = 'TIP03'

        # Cas advectiu del N

        elif (tipus1 == 'N'):
            tipus = 'TIP04'

        # Cas advectiu del NE

        elif (tipus1 == 'NE'):
            tipus = 'TIP05'

        # Cas indeterminat

        elif (tipus1 == 'U'):
            if (tipus2[0] == 'C'):
                if (tipus2 == 'CS' or tipus2 == 'CSW' or tipus2 == 'CSE'):
                    # Cas de gota freda al SW, l'assimilarem al tipus TIP09
                    tipus = 'TIP09'
                else:
                    # Solc
                    tipus = 'TIP10'
            else:
                # Tipus indeterminat: panta barometric o baixa superficial
                tipus = 'TIP12'

        classificacio[dia] = tipus

    return classificacio