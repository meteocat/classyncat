def write_csv(classificacio, csv_file):

    with open(csv_file, 'w') as f: 
        for key, value in classificacio.items():
            f.write('%s;%s\n' % (key, value))
