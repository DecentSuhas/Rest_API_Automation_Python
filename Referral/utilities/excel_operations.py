"""
 This file has all the functions related to excel operation
"""
import openpyxl
from Referral.utilities.config import localization_dict, path

locale_text_list = []
list_of_region = []


def get_ref_text_from_excel(locale):
    excelPath = path + "\\data\\localization.xlsx"
    wb = openpyxl.load_workbook(excelPath)
    counter = 0
    sheet = wb.active
    row = sheet.max_row
    col = sheet.max_column
    global locale_text_list
    for i in range(1, col + 1):
        cell = sheet.cell(row=1, column=i)
        if cell.value == locale:
            for k in range(2, row - 1):
                cell = sheet.cell(row=k, column=i)
                locale_text_list.append(cell.value)
    for key in localization_dict.keys():
        localization_dict[key] = locale_text_list[counter]
        counter = counter + 1


def get_list_of_all_regions():
    excelPath = path + "\\data\\localization.xlsx"
    wb = openpyxl.load_workbook(excelPath)
    counter = 0
    sheet = wb.active
    col = sheet.max_column
    global list_of_region
    for i in range(1, col + 1):
        cell = sheet.cell(row=1, column=i)
        list_of_region.append(cell.value)

