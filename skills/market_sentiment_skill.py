def analyze_sentiment():

    volume = 0.6
    news = 0.7
    funding = 0.5
    social = 0.6

    score = (
        0.4*volume +
        0.3*news +
        0.2*funding +
        0.1*social
    )

    return {
        "sentiment_score": score
    }
