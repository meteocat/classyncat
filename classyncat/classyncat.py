"""Module to implement Classyncat circulation type classification from

Miró et al(2020): Daily atmospheric circulation patterns for Catalonia
                  (northeast Iberian Peninsula) using a modified version of
                  Jenkinson and Collison method.
"""


def classyncat(jc_sfc: str, jc_500: str) -> str:
    """Synoptic circulation classification based on Miró et al., (2020) "Daily
    atmospheric circulation patterns for Catalonia (northeast Iberian Peninsula)
    using a modified version of Jenkinson and Collison method.

    Types:
        - TIP01: Advection W
        - TIP02: Advection W with Anticyclone
        - TIP03: Advection NW
        - TIP04: Advection N
        - TIP05: Advection NE
        - TIP06: Advection E
        - TIP07: Advection E with a cut-off low
        - TIP08: Advection S
        - TIP09: Advection SW
        - TIP10: Trough
        - TIP11: Cyclone
        - TIP12: Undetermined or surface low
        - TIP13: Anticyclone

    Changes to Miró et al., (2020):
        - TIP11 (DANA in the SW) assimilated to TIP09 (SW Advection).
        - TIP13 (Thermal Low) and TIP14 (Barometric swamp) fusioned.
        - TIP16 (Thermal Anticylone) assimilated to TIP13 (Anticyclone).

    Args:
        jc_sfc (str): Jenkinson-Collison surface circulation type.
        jc_500 (str): Jenkinson-Collison 500 hPa circulation type.

    Returns:
        str: Classyncat circulation type.
    """
    cc_type = "None"

    # Slicing for the types in sfc and 500 we construct the new
    # classification
    if jc_sfc == "A":
        if jc_500[0] == "C":
            if jc_500 == "C":
                cc_type = "TIP13"
            elif jc_500 in ["CSW", "CW", "CNW"]:
                cc_type = "TIP02"
            else:
                cc_type = "TIP13"
        elif jc_500[0] == "A":
            if jc_500 == "A":
                cc_type = "TIP13"
            elif jc_500 in ["ASW", "AW", "ANW"]:
                cc_type = "TIP02"
            else:
                cc_type = "TIP13"
        else:
            if jc_500 in ["SW", "W", "NW"]:
                cc_type = "TIP02"
            else:
                cc_type = "TIP13"

    elif jc_sfc in ["AE", "ASE"]:
        if jc_500[0] == "C":
            cc_type = "TIP07"
        else:
            cc_type = "TIP06"
    elif jc_sfc == "AS":
        cc_type = "TIP08"
    elif jc_sfc == "ASW":
        cc_type = "TIP09"
    elif jc_sfc == "AW":
        cc_type = "TIP02"
    elif jc_sfc == "ANW":
        cc_type = "TIP03"
    elif jc_sfc == "AN":
        cc_type = "TIP04"
    elif jc_sfc == "ANE":
        cc_type = "TIP05"
    elif jc_sfc == "C":
        if jc_500[0] == "C":
            cc_type = "TIP11"
        elif jc_500[0] == "A":
            if jc_500 in ["AW", "ASW", "AE", "ASE", "A"]:
                cc_type = "TIP12"
            else:
                cc_type = "TIP11"
        elif jc_500 == "U":
            cc_type = "TIP12"
        else:
            if jc_500 in ["W", "SW", "E", "SE"]:
                cc_type = "TIP12"
            else:
                cc_type = "TIP11"
    elif jc_sfc in ["CE", "CSE"]:
        if jc_500[0] == "C":
            cc_type = "TIP07"
        else:
            cc_type = "TIP06"
    elif jc_sfc == "CS":
        cc_type = "TIP08"
    elif jc_sfc == "CSW":
        cc_type = "TIP09"
    elif jc_sfc == "CW":
        if jc_500[0] == "C":
            cc_type = "TIP10"
        else:
            cc_type = "TIP01"
    elif jc_sfc == "CNW":
        cc_type = "TIP03"
    elif jc_sfc == "CN":
        cc_type = "TIP04"
    elif jc_sfc == "CNE":
        cc_type = "TIP05"
    elif jc_sfc in ["E", "SE"]:
        if jc_500[0] == "C":
            cc_type = "TIP07"
        else:
            cc_type = "TIP06"
    elif jc_sfc == "S":
        cc_type = "TIP08"
    elif jc_sfc == "SW":
        cc_type = "TIP09"
    elif jc_sfc == "W":
        cc_type = "TIP01"
    elif jc_sfc == "NW":
        cc_type = "TIP03"
    elif jc_sfc == "N":
        cc_type = "TIP04"
    elif jc_sfc == "NE":
        cc_type = "TIP05"
    elif jc_sfc == "U":
        if jc_500[0] == "C":
            if jc_500 in ["CS", "CSW", "CSE"]:
                cc_type = "TIP09"
            else:
                cc_type = "TIP10"
        else:
            cc_type = "TIP12"

    return cc_type
