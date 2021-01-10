import pandas as pd
from datetime import datetime


def today():
    today_string = datetime.today().strftime('%Y%m%d')
    return today_string


demo_row_count = 0


def percentage(a, b):
    return round(a / b * 100, 2)


def read_demo_data():
    global demo_row_count
    if demo_row_count < 10:
        demo_row_count += 1
    else:
        from time import sleep
        sleep(10)
        demo_row_count = 1
    data = pd.read_excel(r"data\wb_demo_data.xlsx")
    data = data[data['row'] == demo_row_count]
    data['progress'] = percentage(data['numerator'], data['denominator'])
    data['Process_Name'] = [x[:11].rstrip('--') for x in data['Process_Name']]
    data = data.reset_index()
    return data
