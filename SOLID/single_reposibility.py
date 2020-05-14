"""
Single Responsibility Principle
A class should have one, and only one, reason to change.

“…You had one job” — Loki to Skurge in Thor:
Ragnarok
A class should have only one job.  If a class has more than one responsibility,
it becomes coupled.  A change to one responsibility results to modification of
the other responsibility.
"""

class Employee(object):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def get_name(self) -> str:
        return self.name

    def get_id(self) -> int:
        return self.id

    # It violates the SRP rule
    def save_emp_data(self, name: str, id: int):
        self.name = name
        self.id = id


# SRP

"""
The Employee class violates the SRP.
How does it violate SRP?
SRP states that classes should have one responsibility, here, we can draw out
two responsibilities: Employee database management and Employee properties
management.  The constructor and get_name manage the Employee properties while the
save manages the Employee storage on a database.
How will this design cause issues in the future?
If the application changes in a way that it affects database management
functions. The classes that make use of Employee properties will have to be
touched and recompiled to compensate for the new changes.
You see this system smells of rigidity, it’s like a domino effect, touch one
card it affects all other cards in line.
To make this conform to SRP, we create another class that will handle the sole
responsibility of storing an EmployeeDB to a database:
"""

class EmployeeDetails(object):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def get_name(self) -> str:
        return self.name

    def get_id(self) -> int:
        return self.id

class EmployeeDB(object):
    def __init__(self):
        pass

    def get_employee(self, name: str, id: int) -> EmployeeDetails:
        return EmployeeDetails(name, id)

    def save_emp_details(self, emp: EmployeeDetails):
        print("Employee name {} and ID {} are Saved to DB".format(emp.name, str(emp.id)))

# Disadvantages of SRP is has to be maintained multiple class objects, to avoid use Facade design pattern

"""
When designing our classes, we should aim to put related features together, so
whenever they tend to change they change for the same reason.  And we should try
to separate features if they will change for different reasons. - Steve Fenton
"""

"""
The downside of this solution is that the clients of the this code have to deal
with two classes.  A common solution to this dilemma is to apply the Facade
pattern.  EmployeeDetails class will be the Facade for EmployeeDB database management and
employee properties management.
"""

class EmployeeDetails(object):
    def __init__(self, name: str, id: int, db: EmployeeDB):
        self.name = name
        self.id = id
        self.db = db

    def get_employee_name(self) -> str:
        print("Employee Name is - {}".format(self.name))
        return self.name

    def get_employee_id(self) -> int:
        print("Employee ID id  {}".format(str(self.id)))
        return self.id

    def save_to_db(self):
        self.db.save_emp_details(emp=self)

if __name__ == '__main__':
    # usage of the SRP
    e = EmployeeDetails("User1", 123, EmployeeDB())

    print(e.get_employee_name())

    print(e.get_employee_id())

    e.save_to_db()

    print("completed")

