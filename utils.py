import csv
import json
from abc import ABC, abstractmethod
from faker import Faker

fake = Faker()


class ConfigHandler:
    def __init__(self, config):
        self.config = config

    def get_fields(self):
        return self.config["fields"]

    def get_num_records(self):
        return self.config.get("num_records", 10)

    def get_output_file(self):
        return self.config.get("output_file", "output/data.json")

    def get_file_type(self):
        return self.config.get("file_type", "json")

    def get_delimiter(self):
        return self.config.get("delimiter", ",")


class DataGenerator:
    def __init__(self, fields):
        self.fields = fields

    def _format_value(self, field_name):
        if field_name == "full_name":
            return fake.name()
        elif field_name == "user_id":
            return fake.uuid4()
        elif field_name == "address":
            return {
                "building_no": fake.building_number(),
                "street_address": fake.street_address()
            }
        elif field_name == "product_name":
            return fake.word()
        elif field_name == "category":
            return fake.random_element(elements=["Electronics", "Clothing", "Books", "Home"])
        elif field_name == "Price":
            return fake.pyfloat(left_digits=5, right_digits=2, positive=True)
        elif field_name == "available":
            return fake.boolean()
        elif field_name == "created_at":
            return fake.date_time_this_decade().isoformat()
        else:
            return fake.word()

    def generate_data(self, num_records):
        records = []
        for _ in range(num_records):
            record = {}
            for field in self.fields:
                name = field["field_name"]
                value = self._format_value(name)
                record[name] = value
            records.append(record)
        return records


class FileHandler(ABC):
    def __init__(self, delimiter=','):
        self.delimiter = delimiter

    @abstractmethod
    def write(self, data, output_file):
        pass


class CSVFileHandler(FileHandler):
    def write(self, data, output_file):
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=self.delimiter)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


class JSONFileHandler(FileHandler):
    def write(self, data, output_file):
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)


class FileHandlerFactory:
    @staticmethod
    def get_file_handler(file_type, delimiter=','):
        if file_type == "csv":
            return CSVFileHandler(delimiter)
        elif file_type == "json":
            return JSONFileHandler()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
