import json
import os


class FileService:

    @staticmethod
    def save_data(filename, data):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def load_data(filename):

        if not os.path.exists(filename):
            return []

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)