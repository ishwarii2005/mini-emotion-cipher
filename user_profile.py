user_vocabulary = {}


def learn_user_patterns(text, emotion_dict):
    """
    Learn word-emotion associations from user input.
    """

    words = text.lower().split()

    for word in words:

        if word not in user_vocabulary:
            user_vocabulary[word] = {}

        for emotion in emotion_dict:

            if emotion not in user_vocabulary[word]:
                user_vocabulary[word][emotion] = 0

            user_vocabulary[word][emotion] += 1


def adjust_emotions(text, emotion_dict):
    """
    Adjust emotion scores based on learned user patterns.
    """

    words = text.lower().split()

    for word in words:

        if word in user_vocabulary:

            for emotion in user_vocabulary[word]:

                if emotion in emotion_dict:
                    emotion_dict[emotion] += 0.05

    return emotion_dict