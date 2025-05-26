# department.py

from employee import Employee  # type: ignore # Only if using separate files

class Department:
    def __init__(self, dept_name, employee: Employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: holds reference to an independent Employee object

    def show_department_info(self):
        return f"Department: {self.dept_name} | {self.employee.get_details()}"
