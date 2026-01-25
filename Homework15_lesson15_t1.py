class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width: int, height: int) -> None:
        """Initialize a Rectangle object."""
        self.width = width
        self.height = height

    def get_square(self) -> int:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def __eq__(self, other: "Rectangle") -> bool:
        """Check if two rectangles have the same area."""
        area1 = self.get_square()
        area2 = other.get_square()
        return area1 == area2

    def __add__(self, other: "Rectangle") -> "Rectangle":
        """Add two rectangles by their areas."""
        area1 = self.get_square()
        area2 = other.get_square()
        new_area = area1 + area2
        new_width = 1
        new_height = new_area
        return Rectangle(new_width, new_height)

    def __mul__(self, n: int) -> "Rectangle":
        """Scale the rectangle's area by a factor of n."""
        old_rect_area = self.get_square()
        new_rect_area = old_rect_area * n
        new_width = 1
        new_height = new_rect_area
        return Rectangle(new_width, new_height)

    def __str__(self) -> str:
        """Return string of the Rectangle."""
        return f"Rectangle: width={self.width}, height={self.height}, area={self.get_square()}"