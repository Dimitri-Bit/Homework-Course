class Company:

    def __init__(self, name, area, balance, max_num_of_employees):
        self.__name = name
        self.__area = area
        self.__employees = ()
        self.__balance = balance
        self.__max_num_of_employees = max_num_of_employees

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_area(self):
        return self.__area
    
    def set_area(self, area):
        self.__area = area

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance can not be less then 0")

    def get_max_num_of_employees(self):
        return self.__max_num_of_employees
    
    def set_max_num_of_employees(self, num):
        if num >= 0:
            self.__max_num_of_employees = num
        else:
            print("Maximum number of employees can not be less then 0")

    def add_employee(self, employee):
        if len(self.__employees) < self.__max_num_of_employees:
            self.__employees.append(employee)
        else:
            print("Reached maximum amount of employees")

    def remove_employee(self, name, surname):
        for i in self.__employees:
            employee = self.__employees
            if employee.get("name") == name and employee.get("surname") == surname:
                self.__employees.remove(employee)