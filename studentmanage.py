from students import student_crud as crud
from students import file_handling as fh
class StudentManager:
    def __init__(self):
        self.records = fh.load_data()       # load data when ever calls
        # fh.save_data(self.records)

    def add_student(self,name,roll_no,section,marks):
        a = crud.add_student(self.records,name,roll_no,section,marks)
        if a is not None:
            self.records = a
            fh.save_data(self.records)
            return True
        return False

    def search_student(self,roll_no):
        return crud.search_student(self.records,roll_no)
        
    def delete_student(self,roll_no):
        a = crud.delete_student(self.records,roll_no)
        if a is not None:
            self.records = a
            fh.save_data(self.records)
            return True
        return False

    def update_marks(self,roll_no,marks):
        a = crud.update_marks(self.records,roll_no,marks)
        if a is not None:
            self.records = a
            fh.save_data(self.records)
            return True
        return False    

