import csv
import json
import pathlib

from tabulate import tabulate
import yaml


class CSVHandler:

    @staticmethod
    def read_content(path):
        """Get data from csv to Python dict."""
        lines = list()
        with open(path, 'r') as csv_file:
            dialect = csv.Sniffer().sniff(str(csv_file.readline()), ',; ')
            csv_file.seek(0)
            reader = csv.DictReader(csv_file, dialect=dialect)
            for row in reader:
                lines.append(row)
            return lines

    @staticmethod
    def write_content(data, path):
        """Save data from Python dict to csv."""
        with open(path, 'w', newline='') as new_file:
            writer = csv.DictWriter(new_file,
                                    delimiter=',',
                                    fieldnames=data[0])
            writer.writeheader()
            writer.writerows(data)


class JSONHandler:

    @staticmethod
    def read_content(path):
        """Get data from json to Python dict."""
        with open(path, 'r') as json_file:
            json_data = json.load(json_file)
            return json_data

    @staticmethod
    def write_content(data, path):
        """Save data from Python dict to csv."""
        with open(path, 'w') as new_file:
            json.dump(data, new_file)


class YAMLHandler:

    @staticmethod
    def read_content(path):
        """Get data from yaml to Python dict."""
        with open(path, 'r') as yaml_file:
            yaml_data = yaml.load(yaml_file, Loader=yaml.BaseLoader)
            return yaml_data

    @staticmethod
    def write_content(data, path):
        """Save data from Python dict to csv."""
        with open(path, 'w', newline='') as new_file:
            yaml.dump(data, new_file)


class Converter:
    """Converter from csv/json/yaml to dict and back.

    Args:
        data (:obj:`list` of :obj:`dict`, optional): List of dicts with data,
            which need to convert to.

    Attributes:
        data (:obj:`list` of :obj:`dict`): Python readable data.

    Examples:
        data = Converter()
        data.read('path_to_file.csv')
        data.write('path_to_file.json)

        second_data = Converter([{'key':value}])
        second_data.write('path_to_file.yaml')

    """

    FORMATS = {
        '.csv': CSVHandler,
        '.json': JSONHandler,
        '.yaml': YAMLHandler,
    }

    def __init__(self, data=None):
        self.data = data

    def get_handler(self, path):
        """Get handler from file extension."""
        suffix = pathlib.Path(path).suffix
        return Converter.FORMATS[suffix]

    def read(self, path: str):
        """Read data from file."""
        handler = self.get_handler(path)
        self.data = handler.read_content(path)

    def write(self, path: str):
        """Write data to file."""
        handler = self.get_handler(path)
        handler.write_content(self.data, path)

    def __str__(self):
        return tabulate(
            self.data,
            headers='keys',
            showindex='always',
        )

    def __repr__(self):
        return self.data
