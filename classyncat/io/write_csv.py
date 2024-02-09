"""Module to export Classyncat results.
"""


def write_csv(cc_types: dict, csv_file: str) -> None:
    """
    Write the Classyncat classification output into a csv file.

    Args:
        cc_types (dict): Classyncat types with dates as keys.
        csv_file (str): Output csv file name.
    """
    with open(csv_file, "w", encoding="utf-8") as f:
        for key, value in cc_types.items():
            f.write(f"{key};{value}\n")
