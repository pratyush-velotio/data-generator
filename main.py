# main.py
import json
from utils import ConfigHandler, DataGenerator, FileHandlerFactory


def main():
    # Load configuration
    with open("config.json") as f:
        config = json.load(f)

    config_handler = ConfigHandler(config)
    fields = config_handler.get_fields()
    num_records = config_handler.get_num_records()
    output_file = config_handler.get_output_file()
    file_type = config_handler.get_file_type()
    delimiter = config_handler.get_delimiter()

    # Generate data
    generator = DataGenerator(fields)
    data = generator.generate_data(num_records)

    # Write to file
    file_handler = FileHandlerFactory.get_file_handler(file_type, delimiter)
    file_handler.write(data, output_file)
    print(f"Data written to {output_file} in {file_type} format.")
    print(f"Generated {num_records} records")


if __name__ == "__main__":
    main()
