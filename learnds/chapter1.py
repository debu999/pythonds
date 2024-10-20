"""
This is a module docstring.

It can span multiple lines and is used to describe the purpose and functionality of the module.

Args:
    None

Returns:
    None

Raises:
    None
"""
from pprint import pp

class Cookie:
    """
    This is a class representing a cookie.

    Attributes:
        color (str): The color of the cookie.

    Methods:
        get_color(self) -> str:
            Returns the color of the cookie.

        set_color(self, color):
            Sets the color of the cookie.

        __str__(self):
            Returns a string representation of the cookie.

        __repr__(self):
            Returns a string representation of the cookie.
    """

    def __init__(self, color: str):
        self.color = color

    def get_color(self) -> str:
        """
        Returns the color of the cookie.

        Returns:
            str: The color of the cookie.
        """
        return self.color

    def set_color(self, color: str):
        """
        Sets the color of the cookie.

        Args:
            color (str): The new color of the cookie.

        Returns:
            None
        """
        self.color = color

    def __str__(self):
        return f"Cookie['{self.color}']"

    def __repr__(self):
        return f"Cookie['{self.color}']"



cookie_one = Cookie("green")
cookie_two = Cookie("blue")
cookie_three = Cookie("red")

if __name__ == "__main__":
    pp([cookie_one, cookie_two, cookie_three])
    cookie_one.set_color("pink")
    pp([cookie_one, cookie_two, cookie_three])
