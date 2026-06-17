import student_management
from student_management import records
import os
import json
file_name = 'Student_Records.json'
def load_data():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name,"r") as f:
            new_data = json.load(f)
        new_data.extend(records)
    except json.JSONDecodeError:
         return []
    except FileNotFoundError:
        print("File is not available")
    except Exception as e:
        print(f"Exception is {e}")
    return new_data
def save_data(new_data):
        with open(file_name,"w") as f:
            json.dump(new_data,f)
