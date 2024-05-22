# Gerren Jerome
# This program creates a class registration system. Students log into the class
# registration system and then they can add courses, drop courses, and list the courses
# for which they have registered.


from datetime import datetime

def display_bill(id, s_in_state, c_rosters, c_hours):
    # Determine the tuition rate based on whether the student is in/out of state.
    tuition_rate = 225 if s_in_state[id] else 850
    # Print the tuition summary header with student ID and residency status.
    print("Tuition Summary")
    print("Student: {}, {} Student".format(id, "In-State" if s_in_state[id] else "Out-of-State"))
    # Print generated date and time using the current timestamp.
    print("Generated on", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # Print the table header for course, hours, and cost.
    print("Course    Hours    Cost")
    print("------    -----  --------")
    # Initialize variables to track the total hours and cost.
    total_hours = 0
    total_cost = 0
    # Iterate over the course rosters to calculate the cost for each course the student is enrolled in.
    for course, roster in c_rosters.items():
        if id in roster:
            hours = c_hours[course]
            cost = hours * tuition_rate
            # Update the total hours and cost.
            total_hours += hours
            total_cost += cost
            # print the course details ( course name, hours, and cost )
            print("{:<10} {:>4}  ${:,.2f}".format(course, hours, cost))
    # Print the total line with the aggregated hours and cost
    print("        -------  --------")
    print("Total      {:>4}  ${:,.2f}".format(total_hours, total_cost))