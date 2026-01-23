from exceptions import ErrorCounter
from student import Student


class Group:
    """Represents a group of students."""

    def __init__(self, number: int) -> None:
        """Initialize a Group object.
        
        Args:
            number: Group number
        """
        self.number = number
        self.group = []

    def add_student(self, student: Student) -> None:
        """Add a student to the group.
        
        Args:
            student: Student object to add
        """
        if len(self.group) >= 10:
            raise ErrorCounter
        self.group.append(student)

    def find_student(self, last_name: str) -> Student | None:
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