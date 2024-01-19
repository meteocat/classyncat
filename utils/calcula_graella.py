def calcula_graella(punts: str) -> float:
    """Given the grid points this subroutine calculates
    the central latitude of that.

    Returns:
        float: latitude of the center of grid.
    """
    
    graella = []
    fp = open(punts, 'Ur')
    for line in fp:
        graella.append(line.strip().split(' '))

    lat_nord = float(graella[0][0])
    long_oest = float(graella[0][1])
    lat_sud = float(graella[-1][0])
    long_est = float(graella[-1][1])
    
    mig = (float(lat_sud)+float(lat_nord))/2
    
    rectangle = [lat_nord, long_oest, lat_sud, long_est]

    return mig, rectangle
