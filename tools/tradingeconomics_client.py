import requests
import os


class TradingEconomicsClient:

    def __init__(self):

        self.api_key = os.getenv("TE_API_KEY")

    def get_pmi(self):

        url = "https://api.tradingeconomics.com/pmi/china"

        params = {
            "c": self.api_key
        }

        r = requests.get(url, params=params)

        return r.json()

    def get_cpi(self):

        url = "https://api.tradingeconomics.com/cpi/china"

        params = {
            "c": self.api_key
        }

        r = requests.get(url, params=params)

        return r.json()
