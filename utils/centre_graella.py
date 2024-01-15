def calcula_centre_graella(punts):
    
    graella = []
    fp = open(punts, 'Ur')
    for line in fp:
        graella.append(line.strip().split(' '))

    lat_nord = graella[0][0]
    lat_sud = graella[-1][0]
    mig = (float(lat_sud)+float(lat_nord))/2

    return mig
