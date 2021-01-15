# Python
import re
# data memory
from memory_numbers import memory_numbers


class Display:
    """Class for print type LCD the information given by the user
    """

    def __init__(self, type_data):
        self.type_data = type_data

    def print(self, size, information):
        """method in charge of printing according to the size
           and information given

           @size int = size that must have the impression
           @information str = information given by the user
        """
        # Get number "columns" and "rows"
        column = size + 2
        row = (size * 2) + 3

        total = len(information) * 2 - 1
        # Build structure Display
        top = ''
        body_top = ''
        center = ''
        body_botton = ''
        bottom = ''
        index = 0

        for data in information:
            if self.type_data == 'number':
                structure_data = self.memory(self.type_data, data)
            elif self.type_data == 'letter':
                structure_data = self.memory(self.type_data, data)
            # Top
            top += self.horizontal(structure_data[0], size, column)
            # Body Top
            body_top += self.vertical(structure_data[1], size)
            # center
            center += self.horizontal(structure_data[2], size, column)
            # Body Botton
            body_botton += self.vertical(structure_data[3], size)
            # Botton
            bottom += self.horizontal(structure_data[4], size, column)

            if index < total - 1:
                top += ' '
                body_top += ' '
                center += ' '
                body_botton += ' '
                bottom += ' '
            else:
                top += '\n'
                body_top += '\n'
                center += '\n'
                body_botton += '\n'
                bottom += '\n'

            index += 2

        body_top = body_top * size
        body_botton = body_botton * size
        return(top + body_top + center + body_botton + bottom)

    def horizontal(self, number, size, column):
        """method in charge of structuring the data in a horizontal way
        @number int = defines whether to add a space if is 0 or if is 1 a "-"
        @size int = number of or "-"
        @column int = number of space
        """
        if number == 1:
            return f' {"-" * size} '
        else:
            return f'{" " * column}'

    def vertical(self, number, size):
        """method in charge of structuring the data in a vertical way
        @size int = number of or space
        @number int = define tah type of structure is, exist 3
        """
        if number == 1:
            return f' {" " * size}|'
        elif number == 2:
            return f'| {" " * size}'
        else:
            return f'|{" " * size}|'

    def memory(self, type_data, number):
        """
        """
        if type_data == 'number':
            return memory_numbers.get(number)
        elif type_data == 'letter':
            return memory_letters.get(number)


def validate_lines(lines):
    """Split line and print each

    @lines str = obtains the information given by the user
    return space if is 0,0
    """

    for line in lines:

        line_split = line.split(',')

        if not line == "0,0":
            size = int(line_split[0])
            information = line_split[1]
            # Create instace display
            displays = Display('number')
            print(displays.print(size=size, information=information))
        else:
            return " "

if __name__ == "__main__":
    start_input = True
    lines = ''
    print(
    """
    #######################################
                TEST HABI
    #######################################
    Please enter line, use this format how
    example:  1,23
    the range for fist position is of 1 -10
    to end the program add in the line 0,0
    """)

    while start_input:
        line = input('input: ')
        # validate structure of input
        if not re.match("^(([1-9]|10),[0-9]+|0,0)$", line) and not '0,0' in line:
            # Validate range "size"
            size = line.split(',')[0]
            if not re.match("^([1-9]|10)$", size):
                print(f'The line "{line}" have size "{size}" that is not valid')
            else:
                print(f'The structure of line {line} is not valid')
        else:
            if '0,0' in line:
                start_input = False
                lines += line
            else:
                lines += line.replace(" ", "") + ' '

    print(validate_lines(lines.split(' ')))
