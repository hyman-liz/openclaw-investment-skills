import pandas as pd
from tools.wind_client import WindClient


class SectorRotationSkill:

    def __init__(self):

        self.wind = WindClient()

    def get_sector_data(self):

        data = self.wind.get_industry_data()

        return data

    def calculate_momentum(self, data):

        if data is None:
            return None

        df = pd.DataFrame(data.Data)

        momentum = df.pct_change().mean()

        return momentum

    def run(self):

        data = self.get_sector_data()

        momentum = self.calculate_momentum(data)

        return {
            "sector_momentum": momentum
        }
