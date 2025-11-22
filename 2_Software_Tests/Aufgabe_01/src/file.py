class File:
    @staticmethod
    def create_file(filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            pass

    @staticmethod
    def write_to_file(filename: str, text: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)

    @staticmethod
    def read_from_file(filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    