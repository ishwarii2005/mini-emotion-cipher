from transformers import pipeline

# Load emotion detection model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def detect_emotions(text):

    results = emotion_classifier(text)[0]

    # Sort emotions by confidence
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

    emotions = {}

    # Take top 2 emotions
    for r in sorted_results[:2]:
        emotions[r["label"]] = round(r["score"], 3)

    return emotions