import os
import tushare as ts

token = os.getenv("TUSHARE_TOKEN")
pro = ts.pro_api(token)

def analyze_futures():

    data = pro.fut_basic()

    supply = 0.6
    demand = 0.7
    inventory = 0.5
    macro = 0.6
    sentiment = 0.5
    geo = 0.4

    score = (
        0.25*supply +
        0.25*demand +
        0.2*inventory +
        0.15*macro +
        0.1*sentiment +
        0.05*geo
    )

    return {
        "trend_score": score
    }
