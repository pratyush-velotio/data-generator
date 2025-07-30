import json
import uuid
import datetime
from configuration.config_validation import ConfigModel
from file_utils.file_handler import FileHandlerFactory
from file_utils.utils import DataGenerator
from data_handler.db_handler import DBHandler

def main():
    db = DBHandler()
    print(db.get_metadata("ce5c0f8d-0101-45a5-a342-93d537d4aa0a"))

    try:
        with open("configuration/config.json") as f:
            config_dict = json.load(f)
    except FileNotFoundError:
        print(f"config.json not found in the current directory.")
        return

    try:
        # Validate using Pydantic
        config = ConfigModel(**config_dict)
    except Exception as e:
        print(f"Config validation failed: {e}")
        return

    # Generate data
    output_detail = config.output_details[0]
    handler = FileHandlerFactory.get_handler(output_detail.file_format, output_detail.delimiter)
    generator = DataGenerator([field.model_dump() for field in config.fields])
    data = generator.generate_data(config.num_records) 

    # Save file
    file_id = str(uuid.uuid4())
    filename = output_detail.file_path
    handler.write(data, filename)

    db.insert_metadata(file_id, filename, output_detail.file_format, generated_at=datetime.datetime.now())
    print(f"Metadata is stored in table")
    db.insert_generated_data(data)
    print(f"Data is stored in table")
    # print(f"File ID: {file_id}")
    # print(f"File generated: {filename}")
    
    

if __name__ == "__main__":
    main()
