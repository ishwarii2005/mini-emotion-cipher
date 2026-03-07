from timeline import update_emotion_history, get_emotion_history

update_emotion_history({'joy': 0.82})
update_emotion_history({'sadness': 0.62, 'anger': 0.41})
update_emotion_history({'joy': 0.75})

print(get_emotion_history())