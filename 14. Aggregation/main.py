# main.py (or run this directly)

from department import Department
from employe import Employee


if __name__ == "__main__":
    emp1 = Employee("Ali Khan")             # Independent Employee object
    dept1 = Department("IT", emp1)          # Department uses Employee object (aggregation)

    print(dept1.show_department_info())     # Output: Department: IT | Employee Name: Ali Khan

    # Employee still exists independently
    print(emp1.get_details())               # Output: Employee Name: Ali Khan
