import argparse
import sys
import re
import datetime
import json

# Final Project: College Student Resource Management System 

class Student:
    """
    A class representing a college student with a resource management system.
    """

    def __init__(self, username, password, data_file):

        """
        Initialize a new Student instance.

        Parameters- 
        username: The username of the student.
        password: The password of the student.
        data_file: The file to store student data.
        """
                
        self.username = username
        self.password = password
        self.data_file = data_file
        self.profile = {"name": "", "dob": "", "preferences": ""}
        self.academic_calendar = []
        self.grade_tracker = {"gpa": 0.0, "academic_goals": ""}
        self.task_manager = {"tasks": [], "errands": []}
        self.event_calendar = {"gym_efforts": [], "meeting": [], "other": []}
        self.financial_management = {"budgets": {"weekly": 0.0, "monthly": 0.0}, "expenses": []}

    def display_menu(self):
        """
        Display menu of available options in the student resource manag
        ement system.
        """

        print("\n===== College Student Resource Management System =====")
        print("1. Log In/Sign Up")
        print("2. Update Profile")
        print("3. Update Academic Calendar")
        print("4. Update Grade Tracker")
        print("5. Update Task Manager")
        print("6. Update Event Calendar")
        print("7. Update Financial Management")
        print("8. View Home Screen")
        print("9. Backup Data")
        print("10. Exit")

    def execute_option(self, option):
        """
        Execute the selected option from the menu in command line.
        """
        if option == 1:
            self.log_in()
        elif option == 2:
            self.update_profile()
        elif option == 3:
            self.update_academic_calendar()
        elif option == 4:
            self.update_grade_tracker()
        elif option == 5:
            self.update_task_manager()
        elif option == 6:
            self.update_event_calendar()
        elif option == 7:
            self.update_financial_management()
        elif option == 8:
            self.view_home()
        elif option == 9:
            self.backup_data()
        elif option == 10:
            sys.exit()
        else:
            print("Invalid option. Please try again.")

    def log_in(self):
        """
        Log in student by loading data from UMD Canvas file, and entered information.
        """

        with open(self.data_file, 'r') as file:
            data = json.load(file)

        if self.username not in data or data[self.username]["password"] != self.password:
            print("Invalid username or password. Please try again.")
            sys.exit()

        self.profile = data[self.username]["profile"]
        self.academic_calendar = data[self.username]["academic_calendar"]
        self.grade_tracker = data[self.username]["grade_tracker"]
        self.task_manager = data[self.username]["task_manager"]
        self.event_calendar = data[self.username]["event_calendar"]
        self.financial_management = data[self.username]["financial_management"]

        print(f"Welcome back, {self.profile['name']}!")

    def update_profile(self):
        """
        Update the student's profile information.
        """
        if not self.profile["name"]:
            self.profile["name"] = input("Enter your name: ")
        if not self.profile["dob"]:
            dob = input("Enter your date of birth (MM/DD): ")
            if re.match(r"\d{2}/\d{2}", dob):
                self.profile["dob"] = dob
            else:
                print("Invalid date format. Please use MM/DD.")
                return
        if not self.profile["preferences"]:
            self.profile["preferences"] = input("Enter your preferences: ")

    def update_academic_calendar(self):
        """
        Update the academic calendar with either UMD Canvas integration or self entry.
        """

        print("1. Link UMD Canvas Calendar")
        print("2. Manually Enter Class/Assignment Details")

        choice = input("Choose an option (1 or 2): ")

        if choice == "1":
            print("Linking UMD Canvas Calendar...")
            # In the future- Canvas Calendar integration code would go here
        elif choice == "2":
            course = input("Enter course name: ")
            deadline = input("Enter assignment deadline (MM-DD-YY): ")
            event = {"course": course, "deadline": deadline}
            self.academic_calendar.append(event)
            print("Academic calendar updated successfully.")
        else:
            print("Invalid. Please try again.")

    def update_grade_tracker(self):
        """
        Update the student's grade tracker with GPA and academic goals.
        """

        gpa = float(input("Enter your GPA: "))
        academic_goals = input("Enter your academic goals: ")
        self.grade_tracker["gpa"] = gpa
        self.grade_tracker["academic_goals"] = academic_goals
        print("Grade tracker updated successfully.")

    def update_task_manager(self):
        """
        Update the student's task manager with new tasks and errands.
        """

        task = input("Enter task: ")
        errand = input("Enter errand: ")
        new_task = {"task": task, "completed": False}
        new_errand = {"errand": errand, "completed": False}
        self.task_manager["tasks"].append(new_task)
        self.task_manager["errands"].append(new_errand)
        print("Task manager updated successfully.")

    def update_event_calendar(self):
        """
        Update the student's event calendar with details for gym efforts, meetings, and other events.
        """

        gym_effort = input("Enter gym details: ")
        meeting = input("Enter meeting details: ")
        other = input("Enter other event details: ")
        self.event_calendar["gym_efforts"].append(gym_effort)
        self.event_calendar["meeting"].append(meeting)
        self.event_calendar["other"].append(other)
        print("Event calendar updated successfully.")

    def update_financial_management(self):
        """
        Update the student's financial management with weekly and monthly budgets, as well as expenses.
        """


        weekly_budget = float(input("Enter your weekly budget: "))
        monthly_budget = float(input("Enter your monthly budget: "))
        expense_item = input("Enter expense item: ")
        expense_price = float(input("Enter expense price: "))
        self.financial_management["budgets"]["weekly"] = weekly_budget
        self.financial_management["budgets"]["monthly"] = monthly_budget
        self.financial_management["expenses"].append({"item": expense_item, "price": expense_price})
        print("Financial management updated successfully.")

    def view_home(self):
        """
        Display the student's data on the home screen.
        """

        print("\n===== Student Data =====")
        print("Username:", self.username)
        print("Profile:", self.profile)
        print("Academic Calendar:", self.academic_calendar)
        print("Grade Tracker:", self.grade_tracker)
        print("Task Manager:", self.task_manager)
        print("Event Calendar:", self.event_calendar)
        print("Financial Management:", self.financial_management)

    def backup_data(self):
        """
        Back up the student's data
        """
        with open(self.data_file, 'w') as file:
            data = {
                self.username: {
                    "password": self.password,
                    "profile": self.profile,
                    "academic_calendar": self.academic_calendar,
                    "grade_tracker": self.grade_tracker,
                    "task_manager": self.task_manager,
                    "event_calendar": self.event_calendar,
                    "financial_management": self.financial_management,
                }
        }
        json.dump(data, file)

        print("Data backed up successfully.")
    
def main():
    parser = argparse.ArgumentParser(description="College Student Resource Management System")
    parser.add_argument("username", type=str, help="Student's username")
    parser.add_argument("password", type=str, help="Student's password")
    args = parser.parse_args()

    data_file = "student_data.json"  # Here is where UMD Canvas ELMS would be linked. 
    student = Student(args.username, args.password, data_file)

    while True:
        student.display_menu()
        try:
            option = int(input("Enter option (1-10): "))
            student.execute_option(option)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()