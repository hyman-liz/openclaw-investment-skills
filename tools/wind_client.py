try:
    from WindPy import w
except:
    w = None


class WindClient:

    def __init__(self):

        if w:
            w.start()

    def get_stock_price(self, code):

        if not w:
            return None

        data = w.wsd(code, "close", "ED-5D", "ED")

        return data

    def get_industry_data(self):

        if not w:
            return None

        data = w.wsd(
            "000300.SH",
            "close",
            "ED-30D",
            "ED"
        )

        return data
