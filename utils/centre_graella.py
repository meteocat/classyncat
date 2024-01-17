def calcula_centre_graella(punts: str) -> float:
    """Given the grid points this subroutine calculates
    the central latitude of that.

    Returns:
        float: latitude of the center of grid.
    """
    
    graella = []
    fp = open(punts, 'Ur')
    for line in fp:
        graella.append(line.strip().split(' '))

    lat_nord = graella[0][0]
    lat_sud = graella[-1][0]
    mig = (float(lat_sud)+float(lat_nord))/2

    return mig
