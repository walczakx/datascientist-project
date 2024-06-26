import os
from pymongo import MongoClient
from transformations import uppercase, calculate_hash

# Environment variables
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
MONGO_DB = os.getenv('MONGO_DB', 'processed_files_db')
MONGO_PASS = os.getenv('MONGO_ROOT_PASSWORD', '')
MONGO_USER = os.getenv('MONGO_ROOT_USERNAME', 'root')

# MongoDB setup
client = MongoClient(MONGO_HOST, MONGO_PORT, username=MONGO_USER, password=MONGO_PASS)
db = client[MONGO_DB]
processed_files_collection = db['processed_files']

# Mapping of file path patterns to their associated transformation functions
# you can use multiple transformation, but this is non-optimal solution right now
transformation_map = {
    ("plant_id_1", ".txt"): [uppercase],
    ("plant_id_2", ".png"): [calculate_hash]
}

def normalize(file_path):
    for (identifier, extension), transformations in transformation_map.items():
        if identifier in file_path and file_path.endswith(extension):
            for transformation in transformations:
                transformation(file_path)
            return
    print(f"No transformation rules defined for file: {file_path}")

def process_new_files():
    landing_zone = "/landing_zone"
    for root, dirs, files in os.walk(landing_zone):
        for file in files:
            file_path = os.path.join(root, file)
            if not processed_files_collection.find_one({"file_path": file_path}):
                normalize(file_path)
                processed_files_collection.insert_one({"file_path": file_path})
                print(f"Processed and logged file: {file_path}")
            else:
                print(f"File {file_path} has already been processed.")

def main():
    process_new_files()

if __name__ == "__main__":
    main()