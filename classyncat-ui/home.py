"""Classyncat User Interface.
"""
import io
import json

import earthkit.data
import pandas as pd
import streamlit as st

from classyncat.classyncat import classyncat
from classyncat.io.download_era5 import download_era5
from classyncat.io.grib_points import get_jc_grib_points
from classyncat.jenkinson_collison import (jenkinson_collison_500,
                                           jenkinson_collison_sfc)
from classyncat.utils.grid import get_grid_from_file


@st.cache_data
def convert_df(data_frame: pd.DataFrame) -> str:
    """Convert a Pandas DataFrame into a CSV file

    Args:
        data_frame (pd.DataFrame): Data to save as CSV file.

    Returns:
        str: utf-8 encoded version of `data_frame`.
    """
    return data_frame.to_csv(index=False).encode("utf-8")


config = None

grib_mslp = None
grib_z500 = None
in_grib_z500 = ""


st.title("Classyncat")

st.write(
    "Aquesta interfície permet obtenir la classificació sinòpitca utilitzant la "
    "metodologia Classyncat."
)


tab1, tab2 = st.tabs(["Dades ERA5", "Classificació"])


with tab1:
    st.write(
        "Descàrrega de les dades de l'ERA5 necessàries per al a classificació "
        "sinòptica: pressió mitjana a nivell de mar i el geopotencial a 500 hPa."
    )

    st.write(
        "Per fer-ho, cal indicar la data d'inici i final del període d'interès i un "
        "fitxer de configuració. Aquest darrer ha de ser en format JSON seguint el "
        "format següent:"
    )

    st.json(
        {
            "era5_data_dir": "/tmp",
            "mslp_grid_points": [
                [45.0, -10.0],
                [45.0, 0.0],
                [45.0, 10.0],
                [40.0, -10.0],
                [40.0, 0.0],
                [40.0, 10.0],
                [35.0, -10.0],
                [35.0, 0.0],
                [35.0, 10.0],
            ],
            "z500_grid_points": [
                [45.0, -15.0],
                [45.0, -5.0],
                [45.0, 5.0],
                [40.0, -15.0],
                [40.0, -5.0],
                [40.0, 5.0],
                [35.0, -15.0],
                [35.0, -5.0],
                [35.0, 5.0],
            ],
        },
        expanded=False,
    )

    st.divider()

    st.markdown("##### Configuració")

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(label="Data inici")

    with col2:
        end_date = st.date_input(label="Data final")

    config_file = st.file_uploader(label="Fitxer de configuració", type="json")

    if config_file is not None:
        # Read JSON file
        try:
            config = json.load(config_file)
        except json.JSONDecodeError:
            st.error("Error: Invalid JSON file.")

        st.markdown("###### Paràmetres carregats")
        df = pd.json_normalize(config).T.reset_index()
        df.columns = ["Paràmetre", "Valor"]
        st.dataframe(df, hide_index=True, use_container_width=True)

        st.divider()

        st.markdown("##### Descàrrega")

        st.write(
            "La descàrrega de les dades es gestiona a través de l'API de CDS pot trigar"
            " diversos minuts."
        )

        st.markdown(
            "Es pot seguir el procés de descàrrega en aquest "
            "[enllaç](https://cds.climate.copernicus.eu/cdsapp#!/yourrequests)."
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

        col21, col22 = st.columns([1, 3])

        with col21:
            btn_download_era5 = st.button("Descarrega les dades")

        with col22:
            if btn_download_era5:
                with st.status("Descarregant les dades...", expanded=True) as status:
                    grib_mslp, grib_z500 = download_era5(
                        start_date=start_date,
                        end_date=end_date,
                        area=area,
                        output_dir=config["era5_data_dir"],
                    )
                    st.write("Dades descarregades.")
                    st.write("Fiter MSLP: " + grib_mslp)
                    st.write("Fiter Z500: " + grib_z500)
                    status.update(
                        label="Descàrrega completada!", state="complete", expanded=False
                    )

with tab2:

    st.write(
        "Classificació sinòptica a partir de les dades d'ERA5 utilitzant Classyncat: "
        "pressió mitjana a nivell de mar i el geopotencial a 500 hPa."
    )

    if config is None:

        st.markdown("##### Configuració")

        st.write(
            "Per fer-ho, cal un fitxer de configuració. Aquest darrer ha de ser en "
            "format JSON seguint el format següent:"
        )

        st.json(
            {
                "era5_data_dir": "/tmp",
                "mslp_grid_points": [
                    [45.0, -10.0],
                    [45.0, 0.0],
                    [45.0, 10.0],
                    [40.0, -10.0],
                    [40.0, 0.0],
                    [40.0, 10.0],
                    [35.0, -10.0],
                    [35.0, 0.0],
                    [35.0, 10.0],
                ],
                "z500_grid_points": [
                    [45.0, -15.0],
                    [45.0, -5.0],
                    [45.0, 5.0],
                    [40.0, -15.0],
                    [40.0, -5.0],
                    [40.0, 5.0],
                    [35.0, -15.0],
                    [35.0, -5.0],
                    [35.0, 5.0],
                ],
            },
            expanded=False,
        )

        config_file = st.file_uploader(
            label="Fitxer de configuració", type="json", key="json2"
        )

        with st.expander("Fitxer de configuració d'exemple"):
            st.markdown(
                """
                A mode d'exemple podeu seleccionar el fitxer:
                - /data/RECERCA/devpyram01/classyncat/config_classyncat.json
                """)

        if config_file is not None:
            # Read JSON file
            try:
                config = json.load(config_file)
            except json.JSONDecodeError:
                st.error("Error: Invalid JSON file.")
            uploader_dsbl = False
        else:
            uploader_dsbl = True
    else:
        st.write(
            "S'utilitza el mateix fitxer de configuració que per a la descàrrega de les"
            " dades."
        )
        uploader_dsbl = False

    st.markdown("##### Fitxers grib per a la classificació")

    st.write(
        "Per poder fer la classificació cal carregar els fitxers en format grib "
        "corresponents a la pressió mitjana a nivell de mar i el geopotencial a "
        "500 hPa."
    )

    with st.expander("Fitxers grib d'exemple"):
        st.markdown(
            """
            A mode d'exemple podeu seleccionar els fitxers:
            - /data/RECERCA/devpyram01/classyncat/era5_slp_2024-01-01_2024-01-03.grb
            - /data/RECERCA/devpyram01/classyncat/era5_500_2024-01-01_2024-01-03.grb
            """)

    in_grib_mslp = st.file_uploader("Fitxer MSLP: ", type="grb", disabled=uploader_dsbl)
    in_grib_z500 = st.file_uploader("Fitxer Z500: ", type="grb", disabled=uploader_dsbl)

    btn_classyncat_dsbl = in_grib_mslp is None or in_grib_mslp is None

    btn_classyncat = st.button("Calcula Classyncat", disabled=btn_classyncat_dsbl)

    if btn_classyncat:
        progress_text = "Calculant. Si us plau, esperi."
        progress_bar = st.progress(0, text=progress_text)

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

        buffer = in_grib_mslp.getbuffer()
        stream = io.BytesIO(buffer)
        data = earthkit.data.from_source("stream", stream, batch_size=0)
        in_grib_mslp = data.to_xarray()

        buffer = in_grib_z500.getbuffer()
        stream = io.BytesIO(buffer)
        data = earthkit.data.from_source("stream", stream, batch_size=0)
        in_grib_z500 = data.to_xarray()

        # Process grib files downloaded from ERA5 API
        grid_mslp, grid_z500 = get_jc_grib_points(
            in_grib_mslp, points_mslp, in_grib_z500, points_z500
        )

        progress_step = 1 / len(grid_mslp.keys())
        progress = 0

        # Calculate circulation weather patterns types JC
        classyncat_types = []
        for valid_time, mslp_data in grid_mslp.items():
            # Calculate the Jenkinson & Collison for sfc
            jc_sfc = jenkinson_collison_sfc(mslp_data, lat_0_mslp)
            # Calculate the Jenkinson & Collison for 500 hPa
            jc_500 = jenkinson_collison_500(grid_z500[valid_time], lat_0_z500)
            # Combine both classifications to obtain Classyncat
            classyncat_type = classyncat(jc_sfc, jc_500)

            classyncat_types.append({"data": valid_time, "classyncat": classyncat_type})

            progress += progress_step
            progress_bar.progress(progress, text=progress_text)

        import time
        time.sleep(1)

        progress_bar.empty()

        classyncat_df = pd.DataFrame(classyncat_types)

        st.markdown("##### Resultats")

        st.dataframe(classyncat_df, use_container_width=True, hide_index=True)

        csv = convert_df(classyncat_df)

        st.download_button(
            "Descarrega la classificació",
            csv,
            "classyncat.csv",
            "text/csv",
            key="download-csv",
        )
