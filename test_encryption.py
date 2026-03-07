from encryption import encrypt_message, decrypt_message

text = "I can't believe I failed that test again."
emotion_code = "02|03"

packet = encrypt_message(text, emotion_code)

print("Encrypted Packet:")
print(packet)

message, code = decrypt_message(packet)

print("\nDecrypted Message:", message)
print("Emotion Code:", code)