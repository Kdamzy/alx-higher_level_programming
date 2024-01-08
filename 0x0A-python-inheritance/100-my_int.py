#!/usr/bin/python3
"""class that inherit from integers."""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """Override == opeartor with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with ==."""
        return self.real == value
