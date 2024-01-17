def write_csv(classificacio: dict, csv_file: str) -> None:
    """Write the calculated classification in a csv file

    Args:
        classificacio (dict): dictionary containing the classification
        for each day.
        csv_file (str): Name of the csv file.
    """

    with open(csv_file, 'w') as f:
        for key, value in classificacio.items():
            f.write('%s;%s\n' % (key, value))
