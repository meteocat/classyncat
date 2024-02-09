"""Module to calculate central latitude and extension of grid.
"""


def get_grid_from_file(grid_points: list) -> float:
    """
    Calculate the central latitude and extension given the grid points.

    Args:
        grid_points (list): Grid points tuples [(lat, lon), ...] to calculate
            Jenkinson-Collison circulation type.

    Raises:
        ValueError: If `grid_points` not properly configured as (lat, lon) pairs.

    Returns:
        float: Center latitude of the grid.
    """
    try:
        lat_points = [float(grid_point[0]) for grid_point in grid_points]
        lon_points = [float(grid_point[1]) for grid_point in grid_points]

        lat_n = max(lat_points)
        lat_s = min(lat_points)

        lon_w = min(lon_points)
        lon_e = max(lon_points)
    except IndexError as err:
        raise IndexError(
            "`grid_points` points may not be properly configured. They "
            "must be a list of latitude and longitude coordinate tuples."
        ) from err

    lat_0 = (lat_s + lat_n) / 2

    grid_extension = [lat_n, lon_w, lat_s, lon_e]

    return lat_0, grid_extension
