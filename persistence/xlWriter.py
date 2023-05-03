import openpyxl as xl


class XLWriter:

    # creates a writer object that writes to a xlsx file
    # gets file from app.py
    def __init__(self, file):
        self.wb = xl.load_workbook(file)

