import pprint
import shutil
import pcolor
import os

def clear_screen():
    os.system('cls||clear')


def print_centre(s):
    return s.center(shutil.get_terminal_size().columns)
