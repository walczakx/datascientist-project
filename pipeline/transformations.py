import hashlib
from helpers import read_file_content, write_file_content, generate_output_path

def uppercase(file_path):
    content = read_file_content(file_path, 'r')
    transformed_content = content.upper()
    output_path = generate_output_path(file_path)
    write_file_content(output_path, transformed_content, 'w')

def calculate_hash(file_path):
    content = read_file_content(file_path, 'rb')
    hash_object = hashlib.sha256(content)
    hex_dig = hash_object.hexdigest()
    output_path = generate_output_path(file_path, new_extension='.txt')
    write_file_content(output_path, hex_dig, 'w')
