# import studentmanage as sm
import os
import json
BASH = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASH,"student_records.json")
def load_data():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name,"r",encoding="utf-8") as f:
            new_data = json.load(f)
        return new_data
    except json.JSONDecodeError:
        new_data = []
        return new_data
    except FileNotFoundError:
        print("File is not available")
        return []
    except Exception as e:
        print(f"Exception is {e}")
        return []
def save_data(new_file):
        with open(file_name,"w",encoding="utf-8") as f:
            json.dump(new_file,f)
        
