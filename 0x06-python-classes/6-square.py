class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Method to initialize the square class

        Arguments:
            size: the size of the square
            position: a tuple representing the position of the square
        Raises:
            TypeError: if size is not an integer or position is not a tuple of 2 positive integers
            ValueError: if size is less than zero or position contains negative integers
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(val, int) for val in position) or \
           not all(val >= 0 for val in position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__size = size
        self.__position = position

    def area(self):
        """A method that calculates the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """A method that retrieves the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """A method that retrieves the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           not all(val >= 0 for val in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """A method that prints the square with the character #"""

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
