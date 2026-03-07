from emotion_encoder import encode_emotions

emotion_result = {
    "sadness": 0.72,
    "anger": 0.45
}

encoded = encode_emotions(emotion_result)

print(encoded)