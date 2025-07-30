from faker import Faker

fake = Faker()


class ConfigHandler:
    def __init__(self, config):
        self.config = config

    def get_fields(self):
        return self.config["fields"]

    def get_num_records(self):
        return self.config.get("num_records")

    def get_output_file(self):
        return self.config.get("output_file")
    
    def get_file_type(self):
        return self.config.get("file_type")

    def get_delimiter(self):
        return self.config.get("delimiter")


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






