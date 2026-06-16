
def add_student(records,name,roll_no,section,marks):

#Saving Records directly to file

    for r in records:
        if r["Roll_no"] == roll_no:     
                  
            return records                  #no change if record is existed
        records.append({"Name":name,"Roll_no":roll_no,"Section":section,"Marks":marks})
    
    return None          

#USING CLAS, TWO CLASS VARIABLES ARE DECLARED AS LIST TO STORE student_id and records

        # if self.roll_no in Students.student_ids:
        #             print("\nAlready Saved")                        
        # else:
        #     Students.student_ids.append(self.roll_no)
        #     # Students.records.append({"Name":self.name,
        #     #                 "Roll_no":self.roll_no,
        #     #                 "Section":self.section,
        #     #                 "Marks":self.marks})
        #     Students.records.append(self)

#USING FUNCTION LOAD AND SAVE

        #     data = sr.load_data()
        #     data.append({
        #                     "Name":self.name,
        #                     "Roll_no":self.roll_no,
        #                     "Section":self.section,
        #                     "Marks":self.marks})
        #     sr.save_data(data)


    # data = sr.load_data()
    # for s in data:
    #     if s["Roll_no"] == roll_no:
    #         return "Already saved"
    # data.append({'Name':name,
    #              "Roll_no":roll_no,
    #              'Section':section,
    #               "Marks":marks})
    # sr.save_data(data)
    # return 'saved'
  
    
        
# SEARCHING ID 

def search_student(records,roll_no):
    for r in records:
        if r["Roll_no"] == roll_no:     #if same rolls are eqaul it return the current records
            return r

    return None    # returns empty or no change

#USING CLAS, TWO CLASS VARIABLES ARE DECLARED AS LIST TO STORE student_id and records 

        # if self.roll_no in Students.student_ids:
        #     for i in Students.records[:]:
        #         if self.roll_no == i.roll_no:
        #             print(i.name,i.roll_no,i.section,i.marks)
        #             return
        #     print("Record has been deleted!!")
        # else:
        #     print("Record is not found in the ids!")
#INSIDE FUNCTION LOAD AND SAVE

    # data = sr.load_data()
    # for student in data:
    #     if student['Roll_no'] == roll_no:
    #         return student
    #     sr.save_data(data)
    # return "Not found"

#DELETING STUDENT

def delete_student(records,roll_no):
    for r in records:
        if r["Roll_no"] == roll_no:         # if rolls are same then
            records.remove(r)                  # remove current record
            
            return records                  # returns new data to save
    
    return None    # otherwise no change in records

#USING CLAS, TWO CLASS VARIABLES ARE DECLARED AS LIST TO STORE student_id and records

    # data = sr.load_data() 
        # roll_ = input("Enter the id: ")
        # if self.roll_no in Students.student_ids:
        #     for i in Students.records[:]:
        #         if self.roll_no == i.roll_no:
        #             Delete_Student.deleted_ids.append(i)
        #             Students.records.remove(i)
        #             print(f'{i.name} {i.roll_no} {i.section} {i.marks} is deleted')
        #             return
        #     print("Record had been deleted!")
        # else:
        #     print("The roll is not in the students_ids")
        # sr.save_data(data)

#INSIDE FUNCTION LOAD AND SAVE

    # data = sr.load_data()
    # updated = [s for s in data if s['Roll_no'] != roll_no]
    # for _ in data:
    #     if len(updated) == len(data):
    #         return "not found"
    #     elif _["Roll_no"] == roll_no:
    #         return f"{roll_no} Already Deleted"
        
    # sr.save_data(updated)
    # return "Deleted"



#UPDATING MARKS


def update_marks(records,roll_no,marks):
    #SECOND METHOD WITHOUT ANY FUNCTION
    for r in records:
        if r["Roll_no"] == roll_no:     # checks
            r["Marks"] = marks
                                        # if same change marks
            return records                  #returns changed record to save
    return None    # if not returns old data to save
    # with class 
    
        # if self.roll_no in Students.student_ids:
        #     for i in Students.records:
        #         if self.roll_no == i.roll_no:
        #             i.marks = self.marks
        #             return       
        # for i in Delete_Student.deleted_ids:
        #     if i.roll_no == self.roll_no:
        #         print("Record has been deleted")
        #         return
        # print("Record has not found")
    #WITH FUNCTION, ONE METHOD WITH LOAD AND SAVE INSIDE
    # data = sr.load_data()
    # for s in data:
    #     if s['Roll_no'] == roll_no:
    #         s["Marks"] = marks
    #         sr.sava_data(data)
    #         return "updated"
    # return 'Not found'
    



        
       