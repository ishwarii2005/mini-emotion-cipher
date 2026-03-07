emotion_cache = {}


def get_cached_result(text):
    """
    Check if emotion result exists in cache.
    """

    return emotion_cache.get(text)


def store_result(text, emotion_result):
    """
    Store emotion result in cache.
    """

    emotion_cache[text] = emotion_result