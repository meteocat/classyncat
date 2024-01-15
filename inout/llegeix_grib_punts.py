
from eccodes import (codes_grib_new_from_file, codes_grib_find_nearest,
                     codes_get, codes_release)


def llegeix_grib_punts(input, punts):

    grid_dict = {}
    f = open(input)

    while 1:
        # Read the grid points
        points = []
        fp = open(punts, 'Ur')
        gid = codes_grib_new_from_file(f)
        if gid is None:
            break
        for line in fp:
            points.append(tuple(line.strip().split(' ')))
        grid = []
        for lat, lon in points:
            nearest = codes_grib_find_nearest(gid, float(lat), float(lon))[0]
            grid.append(nearest.value)
        dia = codes_get(gid, "dataDate")

        grid_dict[dia] = grid
        codes_release(gid)

    return grid_dict
