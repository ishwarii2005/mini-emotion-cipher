emotion_history = {}


def update_emotion_history(emotion_dict):
    """
    Update emotion counts for analytics.
    """

    for emotion in emotion_dict.keys():

        if emotion not in emotion_history:
            emotion_history[emotion] = 0

        emotion_history[emotion] += 1


def get_emotion_history():
    """
    Return emotion distribution data.
    """

    return emotion_history