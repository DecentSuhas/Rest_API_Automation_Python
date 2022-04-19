import pandas as pd


def testss():
    list1 = ['jana', 'Sana', 'tommy', 'raveen']
    text = "kd"
    check = ""
    for i in range(0, len(list1)):
        if list1[i] == text:
            check = "True"
    assert check == "True", f"incorrect text found {text}"
    print(f"Hurray found {text}")


def ps():
    df = pd.read_excel(r"C:\Users\320052425\Desktop\Rest_API_Automation_Python\Referral\localization.xlsx")
    localization_dict = {
        "HEADER_TEXT": "",
        "PARAGRAPH_VALUE": "",
        "HOW_IT_WORKS_TEXT": "",
        "HOW_IT_WORKS_DESC": "",
        "DASHBRD_TOP_NAME": "",
        "DASHBRD_TOP_HEADER": "",
        "DASHBRD_BOTTOM_NAME": "",
        "DASHBRD_BOTTOM_HEADER": "",
        "EXPLORE_NAME": "",
        "EXPLORE_TEXT_HEADER": "",
        "PROFILE_NAME": "",
        "PROFILE_TEXT_HEADER": "",
        "TREATMNT_REPRT_BNR_NAME": "",
        "TREATMNT_REPORT_BNR_HEADER": "",
        "DASHBRD_BTM_BTN_DESC": "",
        "EXPLORE_BTN_DESC": "",
        "PROFILE_BTN_DESC": "",
        "TREATMENT_BTN_DESC": ""
    }
    print(len(localization_dict))
    row_count = len(df.index)
    print(row_count)
    for i in range(0, row_count):
        current_row = df.loc[i]
        sampleList = list(current_row)
        s_name = sampleList[1]
        #localization_dict.update()
        for i in range(0,len(s_name)):
            print(s_name[i])


def new():
    df = pd.read_excel(r"C:\Users\320052425\Desktop\Rest_API_Automation_Python\Referral\localization.xlsx")
    row_count = len(df.index)
    element_texts = (df['English']).to_string(index=False)
    localiz_dict = {
        "HEADER_TEXT": "", "PARAGRAPH_VALUE": "", "HOW_IT_WORKS_TEXT": "", "HOW_IT_WORKS_DESC": "",
        "DASHBRD_TOP_NAME": "", "DASHBRD_TOP_HEADER": "", "DASHBRD_BOTTOM_NAME": "",
        "DASHBRD_BOTTOM_HEADER": "", "EXPLORE_NAME": "", "EXPLORE_TEXT_HEADER": "",
        "PROFILE_NAME": "", "PROFILE_TEXT_HEADER": "", "TREATMNT_REPRT_BNR_NAME": "",
        "TREATMNT_REPORT_BNR_HEADER": "", "DASHBRD_BTM_BTN_DESC": "", "EXPLORE_BTN_DESC": "",
        "PROFILE_BTN_DESC": "", "TREATMENT_BTN_DESC": ""
    }
    for i in df.iterrows():
        print(element_texts)


ps()
