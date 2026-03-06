import os
import tushare as ts
import pandas as pd

token = os.getenv("TUSHARE_TOKEN")
pro = ts.pro_api(token)

def select_stocks():

    df = pro.daily()

    df["score"] = (
        0.2*0.6 +
        0.2*0.7 +
        0.2*0.6 +
        0.15*0.7 +
        0.15*0.6 +
        0.1*0.5
    )

    top = df.head(10)

    return top
