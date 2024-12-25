import os
import csv
import sys

from enum import Enum

mainFilePath = "C:\\Users\\gummy\\aditional_projects\\GD_.txt_levelSystem"


class symbols(Enum):
    START = "?"
    END = "!"
    BLOCK = "#"
    SPIKE = ">"
    EMPTY = "."

print(symbols.END.value)
    

