import requests
from textblob import TextBlob


class PolicyMonitorSkill:

    def __init__(self):

        self.policy_sources = [
            "https://www.gov.cn",
            "https://www.ndrc.gov.cn"
        ]

    def fetch_policy_news(self):

        results = []

        for url in self.policy_sources:

            try:

                r = requests.get(url)

                results.append(r.text)

            except:

                pass

        return results

    def analyze_policy_sentiment(self, texts):

        scores = []

        for text in texts:

            blob = TextBlob(text)

            scores.append(blob.sentiment.polarity)

        if not scores:

            return 0

        return sum(scores) / len(scores)

    def run(self):

        texts = self.fetch_policy_news()

        score = self.analyze_policy_sentiment(texts)

        return {
            "policy_sentiment": score
        }
