import os


def create_file(path: str, name: str, content: str):
    f = open(os.path.join(path, name), "w")
    f.write(content)
    f.close()


def delete_file(path: str, name: str):
    full_file_path = os.path.join(path, name)
    if os.path.isfile(full_file_path):
        os.remove(full_file_path)
        print(f"Delete file: {full_file_path}")
    else:
        print(f"Error: file not found: {full_file_path}")
