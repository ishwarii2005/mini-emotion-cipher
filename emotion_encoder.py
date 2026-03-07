emotion_map = {
    "joy": "01",
    "sadness": "02",
    "anger": "03",
    "fear": "04",
    "surprise": "05",
    "disgust": "06",
    "neutral": "07"
}


def encode_emotions(emotion_dict):
    """
    Convert detected emotions to signature codes.
    """

    codes = []

    for emotion in emotion_dict.keys():
        if emotion in emotion_map:
            codes.append(emotion_map[emotion])

    return "|".join(codes)