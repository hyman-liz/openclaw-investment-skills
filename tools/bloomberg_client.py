import pandas as pd

try:
    from xbbg import blp
except:
    blp = None


class BloombergClient:

    def __init__(self):
        pass

    def get_stock_price(self, ticker):

        if blp is None:
            return None

        df = blp.bdp(ticker, "PX_LAST")

        return df

    def get_macro_data(self):

        tickers = [
            "USGG10YR Index",
            "SPX Index",
            "DXY Index",
            "CL1 Comdty"
        ]

        df = blp.bdp(tickers, "PX_LAST")

        return df
