import studentmanage as sm 



def main():
    manage = sm.StudentManager()
    is_running = True
    while is_running:
        try:
            choice = input("\n ------ Students Data ------\n"
                        "\nEnter your Choice:\n"
                        "1. New Students\n"
                        "2. Student Details\n"
                        "3. Delete a Student\n"
                        "4. Marks updating\n"
                        "5. Exit\n")
            
            if not choice.isdigit() or choice not in ['1','2','3','4','5'] :

                print(f"\nEnter valid numbeer! {choice}❌")
                continue
        except Exception as e:
            print(f'Exception is {e}')
        if choice == '1':

            try:
                while True:
                    try:
                        name = input("Enter Your name: ")
                        if not name.replace(" ","").isalpha():
                            print("Please Enter valid name!")
                            continue
                        break
                    # except Exception as e:
                    #     print(f"Exception is {e}")
                    except TypeError:
                        pass
                    except ValueError:
                        print("dugk")
                
                while True:
                    try:
                        roll_no = int(input("Enter Your roll no: "))
                        break
                    except ValueError:
                        print(f"\nWrong  ⚠️  roll_no  ⚠️")
                        print("\nPlease Enter Valid roll_no\n")
                section = input("Enter Your Section: ")

                while True:
                    try:
                        marks = float(input("Enter marks: "))
                        break
                    except ValueError:
                        print(f"\ninvalid marks\n")
        
                
                
            except UnboundLocalError:
                print("Please Enter some Value!!")
            except ValueError:
                
                print("Please Enter a value not a string! ")    
            # except Exception as e:
            #     print(f'Excedptioon is {e}')
            else:
                result = manage.add_student(name,roll_no,section,marks)
                if result:
                    print("Student added successfully!")
                else:
                    print("Already exists.")

        elif choice == '2':
            
            while True:
                try:
                    roll_no = int(input("Enter Roll Number: "))
                    break
                except ValueError:
                    print("Invalid ⚠️ roll_no ⚠️")
                except TypeError:
                    pass
                except Exception as e:
                    print(f"Exception is {e} ")
            
            result = manage.search_student(roll_no)
            if result:
                print(f"{result['Name']} {result['Roll_no']} {result['Section']} {result['Marks']}")
            else:
                print("Not found")
            

        elif choice == '3':
            try:
                while True:
                    try:
                        roll_no = int(input("\nEnter Roll Number: "))
                        break
                    except ValueError:
                        print("Please Enter a value!")
            except Exception as e:
                print(f'Exception is {e}')
            else:    
                result = manage.delete_student(roll_no)
                if result:
                    print("Student deleted successfully!")
                else:
                    print("not found.")

        elif choice == '4':
            while True:
                step = ''
                try:
                    step = 'roll_no'
                    roll_no = int(input("Enter roll_no: "))
                    step = 'marks'
                    marks = float(input("Enter marks to change: "))
                    break
                except ValueError:
                    if step == 'roll_no':
                        print("This not a valid roll_no  ")
                    elif step == 'marks':
                        print("Enter valid marks")
            result = manage.update_marks(roll_no,marks)
            if result:
                print("Marks updated successfully!")
            else:
                print("Failed to update marks.")
        elif choice == '5':
            print("Exited.......")
            is_running = False
if __name__ == '__main__':
    main()                                                                                          