import requests

def analyze_macro():

    gdp = 6.0
    pmi = 50
    rate = 2
    policy = 0.7
    geo = 0.5

    score = (
        0.3*gdp +
        0.2*pmi +
        0.2*rate +
        0.2*policy +
        0.1*geo
    )

    return {
        "macro_score": score
    }
