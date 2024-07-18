import csv
from io import TextIOWrapper
import os
import uuid

UPLOAD_FOLDER = "c:\\xampp\\htdocs\\Room Allocation\\backend\\static\\uploads"

def parse_group_csv(file):
    try:
        filename = str(uuid.uuid4()) + '.csv'
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            reader = csv.DictReader(f)
            group_data = [row for row in reader]
        
        return group_data
    
    except Exception as e:
        print(f"Error parsing group CSV: {str(e)}")
        return None

def parse_hostel_csv(file):
    try:
        filename = str(uuid.uuid4()) + '.csv'
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        
        with open(os.path.join(UPLOAD_FOLDER, filename), 'r') as f:
            reader = csv.DictReader(f)
            hostel_data = [row for row in reader]
        
        return hostel_data
    
    except Exception as e:
        print(f"Error parsing hostel CSV: {str(e)}")
        return None

