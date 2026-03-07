from user_profile import learn_user_patterns, adjust_emotions

text = "ugh this exam again"

emotion_result = {"sadness": 0.72}

learn_user_patterns(text, emotion_result)

new_text = "ugh another assignment"

new_emotions = {"neutral": 0.50}

adjusted = adjust_emotions(new_text, new_emotions)

print(adjusted)