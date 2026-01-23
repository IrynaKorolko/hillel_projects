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

class Group:
    """Represents a group of students."""

    def __init__(self, number: int) -> None:
        """Initialize a Group object.
        
        Args:
            number: Group number
        """
        self.number = number
        self.group = []

    def add_student(self, student: Student):
        """Add a student to the group.
        
        Args:
            student: Student object to add
        """
        self.group.append(student)

    def find_student(self, last_name: str):
        """Find a student by last name.
        
        Args:
            last_name: Last name to search for
            
        Returns:
            Student object if found, None otherwise
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> bool:
        """Deleting a student by the last name.
        
        Args:
            last_name: Last name of student to delete
            
        Returns:
            True if student was deleted, False if not found
        """
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                return True
        return False

    def __str__(self) -> str:
        """Return string representation of the Group."""
        all_students = ""
        for student in self.group:
            all_students += f"{student.last_name} {student.first_name}\n"
        return f'Номер групи:{self.number}\n {all_students}'