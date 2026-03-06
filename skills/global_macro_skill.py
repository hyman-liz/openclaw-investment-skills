from tools.tradingeconomics_client import TradingEconomicsClient
from tools.bloomberg_client import BloombergClient


class GlobalMacroSkill:

    def __init__(self):

        self.te = TradingEconomicsClient()
        self.bbg = BloombergClient()

    def run(self):

        pmi = self.te.get_pmi()

        cpi = self.te.get_cpi()

        market = self.bbg.get_macro_data()

        macro_score = 0

        if pmi:
            macro_score += 0.4

        if cpi:
            macro_score += 0.3

        if market is not None:
            macro_score += 0.3

        return {
            "macro_score": macro_score,
            "pmi": pmi,
            "cpi": cpi
        }
