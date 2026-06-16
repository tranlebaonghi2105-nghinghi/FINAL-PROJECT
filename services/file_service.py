import json
import os


class FileService:

    @staticmethod
    def load_data(filepath):
        if not os.path.exists(filepath):
            return []

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    return []
                return data

        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def save_data(filepath, data):
        try:
            directory = os.path.dirname(filepath)

            if directory and not os.path.exists(directory):
                os.makedirs(directory)

            with open(filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except IOError as error:
            print(f"Error saving file {filepath}: {error}")