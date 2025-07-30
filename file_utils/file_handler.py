from file_handlers.csv_handler import CSVFileHandler
from file_handlers.json_handler import JSONFileHandler

class FileHandlerFactory:
    @staticmethod
    def get_handler(file_format, *args, **kwargs):
        if file_format == 'csv':
            return CSVFileHandler(*args, **kwargs)
        elif file_format == 'json':
            return JSONFileHandler(*args, **kwargs)
        else:
            raise ValueError("Unsupported file format")
