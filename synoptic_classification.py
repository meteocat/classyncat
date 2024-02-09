"""Main script of Classyncat.
"""

from datetime import datetime

from classyncat.classyncat import classyncat
from classyncat.io.download_era5 import download_era5
from classyncat.io.grib_points import get_jc_grib_points
from classyncat.io.write_csv import write_csv
from classyncat.jenkinson_collison import jenkinson_collison_500, jenkinson_collison_sfc
from classyncat.utils.grid import get_grid_from_file
from classyncat.utils.load_config import load_config


if __name__ == "__main__":
    start_date = datetime(2022, 2, 1)
    end_date = datetime(2022, 5, 13)

    # Read the configuration file
    config = load_config("config_classyncat.json")

    if config.keys() < set(
        ["mslp_grid_points", "z500_grid_points", "era5_data_dir", "output_file"]
    ):
        raise KeyError(
            "Configuration file must include, at least, the following keys: "
            "mslp_grid_points, z500_grid_points, era5_data_dir, output_file."
        )

    # Grid points to be used for the Jenkinson and Collison calculations
    points_mslp = config["mslp_grid_points"]
    points_z500 = config["z500_grid_points"]

    # Calculate the center latitude of the grid and its extension for mslp and z500
    lat_0_mslp, extension_mslp = get_grid_from_file(points_mslp)
    lat_0_z500, extension_z500 = get_grid_from_file(points_z500)

    # Maximum extension between mslp and z500
    area = [
        max([extension_mslp[0], extension_z500[0]]),
        min([extension_mslp[1], extension_z500[1]]),
        min([extension_mslp[2], extension_z500[2]]),
        max([extension_mslp[3], extension_z500[3]]),
    ]

    # Download data from ERA5 API
    grib_mslp, grib_z500 = download_era5(
        start_date=start_date,
        end_date=end_date,
        area=area,
        output_dir=config["era5_data_dir"],
    )

    # Process grib files downloaded from ERA5 API
    grid_mslp, grid_z500 = get_jc_grib_points(
        grib_mslp, points_mslp, grib_z500, points_z500
    )

    # Calculate circulation weather patterns types JC
    classyncat_types = {}
    for valid_time, mslp_data in grid_mslp.items():
        # Calculate the Jenkinson & Collison for sfc
        jc_sfc = jenkinson_collison_sfc(mslp_data, lat_0_mslp)
        # Calculate the Jenkinson & Collison for 500 hPa
        jc_500 = jenkinson_collison_500(grid_z500[valid_time], lat_0_z500)
        # Combine both classifications to obtain Classyncat
        classyncat_type = classyncat(jc_sfc, jc_500)

        classyncat_types[valid_time] = classyncat_type

    # Define output file name
    start_date_str = datetime.strftime(start_date, "%Y%m%d")
    end_date_str = datetime.strftime(start_date, "%Y%m%d")
    output_file = config["output_file"].format_map(
        {"start_date": start_date_str, "end_date": end_date_str}
    )

    # Export results as csv file
    write_csv(classyncat_types, output_file)
