class Human:
    """Represents a human with attributes."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        """Initialization of a Human object.
        
        Args:
            gender: Gender of the person
            age: Age of the person
            first_name: First name of the person
            last_name: Last name of the person
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """String representation of the Human."""
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    """Represents a student and extends a Human class."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        """Initialize a Student object.
        
        Args:
            gender: Gender of the student
            age: Age of the student
            first_name: First name of the student
            last_name: Last name of the student
            record_book: Record book number of the student
        """
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __str__(self) -> str:
        """Return string representation of the Student."""
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record Book: {self.record_book}"
    def __eq__(self, other) -> bool:
        """Check equality based on last name."""
        if not isinstance(other, Student):
            return False
        else:
            return str(self) == str(other)
        