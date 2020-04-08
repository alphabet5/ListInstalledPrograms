
import json
from csv import DictWriter


if __name__ == '__main__':
    data = json.load(open('installed_features.json', 'rb'))
    print(len(data))
    keys1 = []
    keys2 = []
    features_to_include = ['VMWare Tools',
                           'Veeam ONE Monitor Server',
                           'Veeam Backup'
                           ]
    write_data = dict()
    fieldnames = ['PSComputerName', 'DisplayName', 'DisplayVersion', 'Publisher']
    with open('output.csv', 'w') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fieldnames, dialect='excel-tab')
        writer.writeheader()
        for computer in data:
            for item in computer['installed_features'] + computer['installed_features2']:
                try:
                    if True:  # any(substring in item['DisplayName'] for substring in features_to_list):
                        write_data = {key: value for key, value in item.items() if key in fieldnames}
                        write_data['PSComputerName'] = computer['PSComputerName']
                        writer.writerow(write_data)
                except:
                    pass

