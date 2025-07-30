import json
from file_handlers.base_handler import FileHandler

class JSONFileHandler(FileHandler):
    def __init__(self, indent=4):
        super().__init__()
        self.indent = indent
    def write(self, data, output_file: str, *args, **kwargs):
        indent = kwargs.get("indent", 4)
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=indent)

    def read(self, input_file):
        with open(input_file, 'r') as f:
            return json.load(f)
        



