from cryptography.fernet import Fernet
import json

# Generate encryption key
key = Fernet.generate_key()

# Create cipher object
cipher = Fernet(key)


def encrypt_message(text, emotion_code):
    """
    Encrypt message and attach emotion metadata.
    """

    encrypted_text = cipher.encrypt(text.encode()).decode()

    packet = {
        "emotion_code": emotion_code,
        "encrypted_text": encrypted_text
    }

    return json.dumps(packet)


def decrypt_message(packet):
    """
    Decrypt encrypted packet and return original message + emotion code.
    """

    data = json.loads(packet)

    encrypted_text = data["encrypted_text"]
    emotion_code = data["emotion_code"]

    decrypted_text = cipher.decrypt(encrypted_text.encode()).decode()

    return decrypted_text, emotion_code