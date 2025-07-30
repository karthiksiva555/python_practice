class Employee:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        print("Get first name of the employee")
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        print(f"Setting the first_name property with value {value}")

        if not value:
            raise ValueError("First name cannot be empty")

        self._first_name = value