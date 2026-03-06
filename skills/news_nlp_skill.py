import requests
from textblob import TextBlob


class NewsNLPSkill:

    def __init__(self):

        self.news_api = "https://newsapi.org/v2/everything"

    def get_news(self, keyword):

        params = {
            "q": keyword,
            "language": "en",
            "sortBy": "publishedAt"
        }

        r = requests.get(self.news_api, params=params)

        data = r.json()

        return data.get("articles", [])

    def analyze_sentiment(self, articles):

        scores = []

        for article in articles:

            text = article.get("title", "")

            sentiment = TextBlob(text).sentiment.polarity

            scores.append(sentiment)

        if not scores:

            return 0

        return sum(scores) / len(scores)

    def run(self, keyword):

        articles = self.get_news(keyword)

        score = self.analyze_sentiment(articles)

        return {
            "keyword": keyword,
            "sentiment_score": score
        }
