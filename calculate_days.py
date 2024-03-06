# Create a function that calculates and returns how many days there are
# between two text strings that represent dates.
# - A text string that represent a date has the format "dd/MM/yyyy".
# - The function will receive two Strings a return an Int.
# - The difference in days will be absolute (the order of the dates does not matter).
# - If one of the two text strings does not represent a correct data, will throw an
# exception.

from re import match
from datetime import datetime

def calculate_days(date_1, date_2):
    format = check_date_format(date_1, date_2)

    if format == True:
        day_1, month_1, year_1 = date_1.split("/")
        day_2, month_2, year_2 = date_2.split("/")

        date_days_1 = datetime(int(year_1), int(month_1), int(day_1))
        date_days_2 = datetime(int(year_2), int(month_2), int(day_2))
        
        result = date_days_1 - date_days_2

        return (result.days) if(date_days_1 > date_days_2) else(-1 * result.days)

def check_date_format(date_1, date_2):
    data_regex = "[0-3][0-9]\\/[0-1][0-9]\\/\\d{4}$"
    
    if match(data_regex, date_1) and match(data_regex, date_2):
        return True
    else:
        print(f"Date format incorrect: \"{date_1}\" or \"{date_2}\" -> \"31/05/2024\".")
        return False


print(calculate_days("01/10/2000", "12/02/2000"))
print(calculate_days("David", "01/10/2000"))
print(calculate_days("01/10/2023", "01/10/2000"))
print(calculate_days("01/10/2000", "01/10/2023"))
