#C:\Users\VGRA\AppData\Local\Programs\Python\Python36-32

# -*-coding:Latin-1 -*
# using
# --> pip install pandas
# --> pip install --upgrade google-api-python-client
# --> pip install xlrd

import os 
import re #regex
import pandas as pd #excel reader

from Day import Day
import datetime as dt

def isDate(arg):
    try:
        dateRegex = r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$"
        isDate = re.search(dateRegex, str(arg)) is not None
    except:
        isDate = False
    finally:
        return isDate


def readFile(filePath):
    NB_DAY_PER_WEEK = 5

    xl = pd.ExcelFile(filePath)
    sheetName = xl.sheet_names[0]
    dataFrame = xl.parse(sheetName)

    result = []
    nbDays = 0

    for j in range(0, dataFrame.shape[1]):
        for i in range(0, dataFrame.shape[0]):
            if isDate(dataFrame.values[i, j]):
                baseDate = dataFrame.values[i, j]

                for days in range(j + 1, j + 1 + NB_DAY_PER_WEEK):
                    date = (baseDate + dt.timedelta(days - (j +1))).date()
                    day = Day(date)

                    if dataFrame.isnull().values[i, days] == False:
                        day.morning = dataFrame.values[i, days]
                    if dataFrame.isnull().values[i+1, days] == False:
                        day.afternoon = dataFrame.values[i+1, days]
                    
                    if(day.isEmpty() == False):
                        result.append(day)
                        nbDays += 1

    return result;
