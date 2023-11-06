class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.
    """

    def add(self, num1, num2):
        """
        Add two numbers together and return the result.

        Args:
            num1 (float): The first operand.
            num2 (float): The second operand.

        Returns:
            float: The result of the addition.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Subtract one number from another and return the result.

        Args:
            num1 (float): The minuend.
            num2 (float): The subtrahend.

        Returns:
            float: The result of the subtraction.
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Multiply two numbers together and return the result.

        Args:
            num1 (float): The first factor.
            num2 (float): The second factor.

        Returns:
            float: The result of the multiplication.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Divide one number by another and return the result.

        Args:
            num1 (float): The dividend.
            num2 (float): The divisor.

        Returns:
            float: The result of the division.

        Raises:
            ValueError: If the divisor is zero.
        """
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2
