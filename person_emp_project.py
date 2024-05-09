class Person:
    def __init__(self, name, address, age, gender):
        self.name = name
        self.address = address
        self.age = age
        self.gender = gender

    def get_data(self):
        return {
            'Name': self.name,
            'Address': self.address,
            'Age': self.age,
            'Gender': self.gender
        }

    def display_data(self):
        data = self.get_data()
        for key, value in data.items():
            print(f"{key}: {value}")


class Student(Person):
    def __init__(self, name, address, age, gender, class_enrolled, SRN):
        super().__init__(name, address, age, gender)
        self.class_enrolled = class_enrolled
        self.SRN = SRN

    def get_data(self):
        data = super().get_data()
        data['Class Enrolled'] = self.class_enrolled
        data['SRN'] = self.SRN
        return data


class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def get_data(self):
        return {
            'Name': self.name,
            'Designation': self.designation
        }

    def display_data(self):
        data = self.get_data()
        for key, value in data.items():
            print(f"{key}: {value}")


class Project:
    def __init__(self, project_id, title):
        self.project_id = project_id
        self.title = title

    def get_data(self):
        return {
            'Project ID': self.project_id,
            'Title': self.title
        }

    def display_data(self):
        data = self.get_data()
        for key, value in data.items():
            print(f"{key}: {value}")


class Emp_Proj(Employee, Project):
    def __init__(self, name, designation, project_id, title, duration):
        Employee.__init__(self, name, designation)
        Project.__init__(self, project_id, title)
        self.duration = duration

    def get_data(self):
        data = Employee.get_data(self)
        data.update(Project.get_data(self))
        data['Duration'] = self.duration
        return data


def main():
    employees_projects = []
    while True:
        print("\n1. Add Employee and Project details")
        print("2. Display Project details in ascending order of duration")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter employee name: ")
            designation = input("Enter employee designation: ")
            project_id = input("Enter project ID: ")
            title = input("Enter project title: ")
            duration = int(input("Enter project duration: "))
            emp_proj = Emp_Proj(name, designation, project_id, title, duration)
            employees_projects.append(emp_proj)
            print("Employee and Project details added successfully!")
        elif choice == 2:
            sorted_projects = sorted(employees_projects, key=lambda x: x.duration)
            print("\nProject Details in ascending order of duration:")
            for project in sorted_projects:
                project.display_data()
                print()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()