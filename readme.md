# File Transformation Pipeline with Python and MongoDB

## Overview

This project sets up a file transformation pipeline using Python and MongoDB. The pipeline detects new files in a `landing_zone` directory, applies customer-specific transformations, and saves the results in a `data_lake` directory. The state of processed files is stored in a MongoDB database to avoid reprocessing.

## Features

- Detects new files in the `landing_zone` directory.
- Applies customer-specific transformations:
  - Text files from `plant_id_1` are converted to upper case.
  - PNG files from `plant_id_2` are converted to their SHA256 hash.
- Saves transformed files in the `data_lake` directory.
- Stores the state of processed files in a MongoDB database.
- Persistent storage for both data and database.

## Directory Structure

```
project/
├── .env
├── docker compose.yml
├── readme.md
├── pipeline/
│ ├── __init__.py
│ ├── Dockerfile
│ ├── helpers.py
│ ├── pipeline.py
│ ├── requirements.txt
│ └── transformations.py
├── landing_zone/
│ ├── plant_id_1/
│ └── plant_id_2/
├── data_lake/
│ ├── plant_id_1/
│ └── plant_id_2/
└── db_data/
```


## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

**Clone the repository:**

```
git clone <repository_url>
cd project
```

Prepare the directories:
Make sure the following directories exist:

```
    data/landing_zone/plant_id_1/
    data/landing_zone/plant_id_2/
    data/data_lake/plant_id_1/
    data/data_lake/plant_id_2/
    db_data/
```

```
    mkdir -p data_lake/plant_id_1
    mkdir -p data_lake/plant_id_2
    mkdir -p landing_zone/plant_id_1
    mkdir -p landing_zone/plant_id_2
    mkdir -p db_data
```

Build and start the containers:

`docker compose up --build --exit-code-from pipeline`

**Configuration**
please adjust values in .env file. Any other changes at this point are not neccessary

```
    MONGO_DB=processed_files_db
    MONGO_ROOT_PASSWORD=example
    MONGO_ROOT_USERNAME=root
```

**Usage**

    Place files in the landing zone:

    For plant_id_1, place .txt files in data/landing_zone/plant_id_1/.
    For plant_id_2, place .png files in data/landing_zone/plant_id_2/.

    Run the application:

`docker compose up --exit-code-from pipeline`

    Check the transformed files:

    Transformed files for plant_id_1 will be in data/data_lake/plant_id_1/.
    Transformed files for plant_id_2 will be in data/data_lake/plant_id_2/.

If you want, you can keep the database running in background and run on demand only pipeline container. Then commands will be:
`docker compose up -d`
`docker run datascientist-project-pipeline-1`

**Security**
Application nor database expose any ports

**Cleanup**

To stop and remove the containers, run:

`docker compose down`

**Contributing**
Nah

**License**
Nah

# AWS Migration options

## DB
https://aws.amazon.com/blogs/database/performing-a-live-migration-from-a-mongodb-cluster-to-amazon-dynamodb/

## Main app
can be run as:
Lambda on demand - changes releated to storage are neccessary
ECS/EKS as service - in addtion to storage changes mention above, main app 'pipeline.py' should be adjusted to run in loop

## Storage
Use S3 (probably preferable) or NFS, whatever suits your and your data scientist needs.

## Automation
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
