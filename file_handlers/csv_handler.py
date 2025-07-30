import csv
from file_handlers.base_handler import FileHandler

class CSVFileHandler(FileHandler):
    def __init__(self, delimiter=","):
        super().__init__(delimiter)
        self.delimiter = delimiter

    def write(self, data, output_file: str, *args, **kwargs):
        delimiter = kwargs.get("delimiter", self.delimiter)
        fieldnames = list(data[0].keys())
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(data)

    def read(self, input_file):
        with open(input_file, 'r') as f:
            return list(csv.DictReader(f, delimiter=self.delimiter))
        
