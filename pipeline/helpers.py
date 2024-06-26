import os

def read_file_content(file_path, mode='r'):
    with open(file_path, mode) as file:
        return file.read()

def write_file_content(file_path, content, mode='w'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode) as file:
        file.write(content)

def generate_output_path(file_path, new_extension=None):
    output_path = file_path.replace('landing_zone', 'data_lake')
    if new_extension:
        output_path = os.path.splitext(output_path)[0] + new_extension
    return output_path