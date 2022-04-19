"""
 This file has all the functions related to excel operation
"""
import openpyxl

locale_text_list = []


def get_ref_text_from_excel(locale):
    wb = openpyxl.load_workbook(r"C:\Users\320052425\Desktop\Rest_API_Automation_Python\Referral\localization.xlsx")
    sheet = wb.active
    row = sheet.max_row
    col = sheet.max_column
    global locale_text_list
    for i in range(1, col):
        cell = sheet.cell(row=1, column=i)
        if cell.value == "English":
            for k in range(2, row - 1):
                cell = sheet.cell(row=k, column=i)
                locale_text_list.append(cell.value)


get_ref_text_from_excel("English")



# Test test test