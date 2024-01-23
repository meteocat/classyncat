"""Module to calculate spatial grid.
"""


def get_grid_from_file(file_points: str) -> float:
    """Given the grid points this subroutine calculates
    the central latitude of that.

    Returns:
        float: latitude of the center of grid.
    """
    grid_points = []
    with open(file_points, "Ur", encoding="utf-8") as f_p:
        for line in f_p:
            grid_points.append(line.strip().split(" "))

    try:
        lat_points = [float(grid_point[0]) for grid_point in grid_points]
        lon_points = [float(grid_point[1]) for grid_point in grid_points]

        lat_n = max(lat_points)
        lat_s = min(lat_points)

        lon_w = min(lon_points)
        lon_e = max(lon_points)
    except ValueError as err:
        raise ValueError(
            "`file_points` points may not be properly configured. They "
            "must be latitude and longitude coordinates separated by a "
            "white space and each point in a new line."
        ) from err

    center = (lat_s + lat_n) / 2

    grid_extension = [lat_n, lon_w, lat_s, lon_e]

    return center, grid_extension
