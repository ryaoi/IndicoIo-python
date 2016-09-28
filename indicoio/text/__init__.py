from importlib import import_module
TEXT_APIS = {
    name: getattr(import_module(".{0}".format(name), package="indicoio.text"), name)
        for name in [
            "language",
            "personality",
            "political",
            "summarization",
            "twitter_engagement",
            "emotion",
            "organizations",
            "personas",
            "relevance",
            "text_features",
            "keywords",
            "people",
            "places",
            "sentiment",
            "sentiment_hq",
            "text_tags"
        ]
}
globals().update(TEXT_APIS)
