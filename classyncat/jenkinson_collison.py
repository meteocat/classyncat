"""Module to calculate Jenkinson-Collison circulation type"""
import numpy as np


def __jenkinson_collison_parameters(grid: np.array, lat_0: float) -> list:
    """Calculation of Jenkinson-Collison parameters: zonal and meridional components,
    wind direction, wind speed, and vorticity.

    Args:
        grid (np.array): Mean Sea Level Pressure or Geopotential Height data.
        lat_0 (float): Central latitude, in degrees.

    Returns:
        list: w (zonal component), s (meridional component), d (direction),
              f (wind speed), z (vorticity)
    """
    sf_constant = 1 / (2 * np.cos(np.deg2rad(lat_0)))
    zs_constant = 1 / (np.cos(np.deg2rad(lat_0)))
    zw_constant_1 = np.sin(np.deg2rad(lat_0)) / np.sin(np.deg2rad(lat_0 - 2.5))
    zw_constant_2 = np.sin(np.deg2rad(lat_0)) / np.sin(np.deg2rad(lat_0 + 2.5))

    # Change pressure scale (Pa -> hPa)
    p = np.array(grid) / 100.0

    # Wind components
    w = (1.0 / 4.0) * (p[6] + 2 * p[7] + p[8]) - (1.0 / 4.0) * (p[0] + 2 * p[1] + p[2])
    s = sf_constant * (
        (1.0 / 4.0) * (p[2] + 2 * p[5] + p[8]) - (1.0 / 4.0) * (p[0] + 2 * p[3] + p[6])
    )

    # Angle and strength of the flux
    d = np.arctan(w / s) * (180 / np.pi)
    f = np.sqrt(pow(w, 2) + pow(s, 2))

    # Vorticity calculations
    zw = zw_constant_1 * (
        (p[6] + 2 * p[7] + p[8]) - (p[3] + 2 * p[4] + p[5])
    ) - zw_constant_2 * ((p[3] + 2 * p[4] + p[5]) - (p[0] + 2 * p[1] + p[2]))
    zs = zs_constant * (
        0.25 * (p[2] + 2 * p[5] + p[8])
        - 0.25 * (p[1] + 2 * p[4] + p[7])
        - 0.25 * (p[1] + 2 * p[4] + p[7])
        + 0.25 * (p[0] + 2 * p[3] + p[6])
    )
    z = zw + zs

    return w, s, d, f, z


def __jenkinson_collison_fluxes(d: float, s: float, w: float) -> str:
    if -22.5 <= d < 22.5:
        if s > 0:
            direction = "S"
        else:
            direction = "N"
    elif 22.5 <= d < 67.5:
        if w > 0:
            direction = "SW"
        else:
            direction = "NE"
    elif 67.5 <= d <= 112.5:
        if w > 0:
            direction = "W"
        else:
            direction = "E"
    elif -67.5 <= d < -22.5:
        if w > 0:
            direction = "NW"
        else:
            direction = "SE"
    elif -112.5 <= d < -67.5:
        if w > 0:
            direction = "W"
        else:
            direction = "E"
    else:
        direction = None

    return direction


def jenkinson_collison_sfc(grid: np.array, lat_0: float) -> str:
    """Calculate the Jenkinson-Collison type using Mean Sea Level Pressure data
    following:

    Dessouky & Jenkinson(1975): An objective daily catalogue of surface pressure, flow,
    and vorticity indices for Egypt and it’s use in monthly rainfall forecasting.
    Meteorological Research Bulleting, Egypt, 11, 1-25.

    Args:
        grid (np.array): Mean Sea Level Pressure data.
        lat_0 (float): Central latitude, in degrees.

    Returns:
        str: Jenkinson-Collison type.
    """
    w, s, d, f, z = __jenkinson_collison_parameters(grid, lat_0)

    direction = __jenkinson_collison_fluxes(d, s, w)

    if np.abs(z) < f:
        jc_type = direction

    if np.abs(z) > 2 * f:
        if z > 0:
            jc_type = "C"
        else:
            jc_type = "A"
    if np.abs(z) > f and np.abs(z) < 2 * f:
        if z > 0:
            jc_type = "C" + direction
        else:
            jc_type = "A" + direction
    if f < 6 and np.abs(z) < 6:
        jc_type = "U"

    return jc_type


def jenkinson_collison_500(grid: np.array, lat_0: float) -> str:
    """Calculate the Jenkinson-Collison type using Geopotential Height at 500 hPa data
    following:

    Dessouky & Jenkinson(1975): An objective daily catalogue of surface pressure, flow,
    and vorticity indices for Egypt and it’s use in monthly rainfall forecasting.
    Meteorological Research Bulleting, Egypt, 11, 1-25.

    In this case, the threshold to discriminate between cyclonic and anticylconic cases
    is different compared to SFC case, since low curvature cases are considered
    cyclonic.

    Args:
        grid (np.array): Geopotential Height at 500 hPa data.
        lat_0 (float): Central latitude, in degrees.

    Returns:
        str: Jenkinson-Collison type.
    """
    # Change scale pressure (m -> dam)
    w, s, d, f, z = __jenkinson_collison_parameters(grid, lat_0)

    direction = __jenkinson_collison_fluxes(d, s, w)

    # Cyclonic case
    if z > 0:
        if np.abs(z) <= (3.0 / 8.0) * f:
            jc_type = direction

    # Anticyclonic case
    if z <= 0:
        if np.abs(z) <= (4.0 / 3.0) * f:
            jc_type = direction

    if np.abs(z) > 6 * f:
        if z > 0:
            jc_type = "C"
        else:
            jc_type = "A"

    # Cyclonic case
    if z > 0:
        if np.abs(z) > (3.0 / 8.0) * f and np.abs(z) < 6 * f:
            jc_type = "C" + direction
    # Anticyclonic case
    if z <= 0:
        if np.abs(z) > (4.0 / 3.0) * f and np.abs(z) < 6 * f:
            jc_type = "A" + direction

    # Undetermined
    if f < 6 and np.abs(z) < 6:
        jc_type = "U"

    return jc_type
