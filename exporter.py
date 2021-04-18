import csv
import json

class Exporter:
    def generateType(self, data):
        pass

class TypeExporter(Exporter):
    def generateType(self, data = []):
        file_name = 'covid_data.csv'

        json_data = json.dumps(data)

        parsed_data = json.loads(json_data)

        data_file = open(file_name, 'w')

        csv_writer = csv.writer(data_file)

        count = 0
        
        for i in parsed_data:
            if count == 0:
                header = i.keys()
                csv_writer.writerow(header)
                count += 1

            csv_writer.writerow(i.values())
        
        data_file.close()
        
        CSVPlotter().plot_data(file_name)

class CSVPlotter:
    def plot_data(self, csv_data):
        print(f'GRAFICANDO CON {csv_data}')