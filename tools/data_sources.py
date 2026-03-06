import tushare as ts
import os

token = os.getenv("TUSHARE_TOKEN")
pro = ts.pro_api(token)

def get_stock_data():

    return pro.daily()
