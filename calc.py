import math

class Calculator:
    def __init__(self):
        pass

    def calculate(self, expression):
        ...

    def solve_quadratic_equation(self, a, b, c):
        """Solves a quadratic equation of the form ax^2 + bx + c = 0.

        Args:
            a: The coefficient of the x^2 term.
            b: The coefficient of the x term.
            c: The constant term.

        Returns:
            A tuple of two floats, representing the two solutions to the quadratic equation.
        """

        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            # The quadratic equation has complex roots.
            return complex(-b / (2 * a), math.sqrt(-discriminant) / (2 * a)), \
                   complex(-b / (2 * a), -math.sqrt(-discriminant) / (2 * a))
        else:
            # The quadratic equation has real roots.
            return (-b + math.sqrt(discriminant)) / (2 * a), \
                   (-b - math.sqrt(discriminant)) / (2 * a)

if __name__ == "__main__":
    calculator = Calculator()

    # Get input from the user
    user_input = input("Enter operands and operator (e.g., 1+1 or solve_quadratic_equation(1, 2, 1)): ")

    # Calculate and display the result
    if user_input.startswith("solve_quadratic_equation"):
        # Split the input string into the coefficients of the quadratic equation
        coefficients = user_input.split("(")[1][:-1].split(", ")

        # Solve the quadratic equation and display the solutions
        solutions = calculator.solve_quadratic_equation(*coefficients)
        print(f"The solutions to the quadratic equation are:")
        print(solutions[0])
        print(solutions[1])
    else:
        # Calculate and display the result of the arithmetic expression
        result = calculator.calculate(user_input)
        print(result)