
from csv import DictReader


if __name__ == '__main__':
    rows = list()
    with open('output.csv', 'r') as csvfile:
        reader = DictReader(csvfile, dialect='excel-tab')
        for row in reader:
            rows.append(row)

    display_names = list()
    for row in rows:
        display_names.append(row['DisplayName'])
    display_names = set(display_names)
    print(display_names)
    output = dict()
    for display_name in display_names:
        output[display_name] = dict()
        for row in rows:
            if row['DisplayName'] == display_name:
                if 'DisplayName' in row.keys():
                    if row['DisplayVersion'] in output[display_name].keys():
                        output[display_name][row['DisplayVersion']].append(row['PSComputerName'])
                    else:
                        output[display_name][row['DisplayVersion']] = [row['PSComputerName']]
                else:
                    if 'NoVersion' in output[display_name].keys():
                        output[display_name]['NoVersion'].append(row['PSComputerName'])
                    else:
                        output[display_name]['NoVersion'] = [row['PSComputerName']]

    for product, items in output.items():
        for version, servers in items.items():
            print(product, '\t', version, '\t"', '\n'.join(servers), '"')

