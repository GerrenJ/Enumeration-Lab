# Gerren Jerome
# This program creates a class registration system. Students log into the class
# registration system and then they can add courses, drop courses, and list the courses
# for which they have registered.

def add_course(id, c_roster, c_max_size):
    # Prompt the user to enter the course they want to add
    course = input("Enter the course you want to add: ")
    # Check if the course exists in the course roster
    if course not in c_roster:
        print("Course not found.")
        return
    # Check if the student is already enrolled in the course
    if id in c_roster[course]:
        print("You are already enrolled in that course.")
        return
    # Check if the course is already full
    if len(c_roster[course]) >= c_max_size[course]:
        print("Course already full.")
        return
    # Add the student to the course's roster
    c_roster[course].append(id)
    print("Student {} added to the course {}.".format(id, course))


def drop_course(id, c_roster):
    # Prompt the user to enter the course they want to drop
    course = input("Enter the course you want to drop: ")
    # Check if the course exists in the course roster
    if course not in c_roster:
        print("Course not offered.")
        return
    # Check if the student is enrolled in the course
    if id not in c_roster[course]:
        print("You are not enrolled in that course.")
        return
    # Remove the student from the course's roster
    c_roster[course].remove(id)
    print("Student {} dropped from the course {}.".format(id, course))


def list_courses(id, c_roster):
    count = 0
    courses = []
    # Iterate over the course roster to find courses the student is registered for
    for course, roster in c_roster.items():
        if id in roster:
            count += 1
            courses.append(course)
    # Display the number of courses registered and the list of courses
    print("Number of courses registered: {}".format(count))
    print("Courses registered: {}".format(", ".join(courses)))