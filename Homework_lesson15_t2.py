class Fraction:
    """Represents a fraction with different operations."""

    def __init__(self, a: int, b: int):
        """Initialize a fraction object."""

        self.a = a
        self.b = b

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiply two fractions."""
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other: "Fraction") -> "Fraction":
        """Add two fractions."""
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtract two fractions."""
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __eq__(self, other: object) -> bool:
        """Check if two fractions are equal."""
        if not isinstance(other, Fraction):
            return False
        return self.a * other.b == other.a * self.b

    def __gt__(self, other: "Fraction") -> bool:
        """Check if this fraction is greater than another."""
        return self.a * other.b > other.a * self.b

    def __lt__(self, other: "Fraction") -> bool:
        """Check if this fraction is less than another."""
        return self.a * other.b < other.a * self.b

    def __str__(self) -> str:
        """Return string representation of the fraction."""
        return f"Дріб: {self.a}/{self.b}"