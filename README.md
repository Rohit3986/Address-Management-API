﻿# Address-Management-API

Features
Create a new address record with the specified details.
Retrieve a specific address record by ID.
Retrieve all addresses which belongs to a specific STATE.
List all address records.
Update an existing address record.
Delete an address record.

Installation
-Clone the repository


Install the dependencies using pip:
-pip install -r requirements.txt

Set up the MySQL database:

Create a MySQL database using a tool of your choice.
Update the database connection details in the config.py file.

Run the API server:
-uvicorn main:app --reload

API Endpoints
POST /add_address: Create a new address record.

GET /get_address_by_address_id/{address_id}:Retrieve a specific address record by ID.

GET /get_all_entries: List all address records.

PATCH /update_address/{address_id}: Update an existing address record.

DELETE /delete_address/{address_id}: Delete an address record.
