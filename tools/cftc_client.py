from pycot.reports import CommitmentOfTraders


class CFTCClient:

    def __init__(self):

        self.cot = CommitmentOfTraders("legacy_fut")

    def get_cot_data(self, market):

        df = self.cot.report((market,))

        return df
