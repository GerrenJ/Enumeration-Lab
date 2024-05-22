# Gerren Jerome
# This program creates a class registration system. Students log into the class
# registration system and then they can add courses, drop courses, and list the courses
# for which they have registered.


import student
import billing


def login(id, s_list):
    # Prompt the user to enter the PIN.
    pin = input("Enter PIN: ")
    # Check if the ID and OIN combination exists in the student list.
    for student_id, student_pin in s_list:
        if student_id == id and student_pin == pin:
            print("ID and PIN verified")
            return True

    print("ID or PIN incorrect")
    return False


def main():
    # Initialized student data.
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True, '1002': False, '1003': True, '1004': False}
    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    while True:
        id = input("Enter ID to log in, or 0 to quit: ")

        if id == '0':
            break

        if login(id, student_list):
            while True:
                # Prompt the user to enter a choice.
                print("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit:")
                choice = input()

                if choice == '1':
                    # Call add_course function from student.py module.
                    student.add_course(id, course_roster, course_max_size)
                elif choice == '2':
                    # Call drop_course function from the student.py module.
                    student.drop_course(id, course_roster)
                elif choice == '3':
                    # Call list_courses function from the student.py module.
                    student.list_courses(id, course_roster)
                elif choice == '4':
                    # Call display_bill function from the billing.py module.
                    billing.display_bill(id, student_in_state, course_roster, course_hours)
                elif choice == '0':
                    break
                else:
                    print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()