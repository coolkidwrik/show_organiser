import openpyxl as xl


class XLReader:

    # creates a reader object that reads from a xlsx file
    # gets file from app.py
    def __init__(self, file):
        self.wb = xl.load_workbook(file)

