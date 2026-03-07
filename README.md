# Mini Emotion Cipher
## Hosted on- https://mini-emotion-cipher-ish.streamlit.app/
## Demo- https://drive.google.com/drive/folders/1L6kKhELLTQFgQuRr2KPKZEEK-aPKp_B2?usp=sharing

Mini Emotion Cipher is a privacy-preserving system that detects the emotional context of a message while keeping the actual text encrypted.

The idea is simple:  
even when the message is protected, the emotional signal can still be used for analytics, moderation, or insights.

---

## What the System Does

1. User enters a message
2. The system detects emotions using a transformer model
3. The message is encrypted using AES
4. Emotional metadata is encoded and attached to the encrypted packet
5. The message can be decrypted later while preserving the emotion signature

---

## Key Features

- **Transformer-based Emotion Detection**  
  Uses a DistilRoBERTa emotion model for accurate emotion classification.

- **Multi-Emotion Detection**  
  Extracts the top two emotions with confidence scores.

- **Emotion Metadata Encoding**  
  Emotional signals are encoded as lightweight emotion codes.

- **Secure AES Encryption**  
  The original message is encrypted to ensure privacy.

- **Emotion-Aware Decryption**  
  Decryption restores both the message and the detected emotional context.

- **Multilingual Input Support**  
  Messages in different languages are translated before emotion detection.

- **Emotion Caching**  
  Previously analyzed messages are cached for faster processing.

- **Adaptive User Vocabulary Learning**  
  The system gradually learns patterns in how a user expresses emotions.

- **Emotion Analytics Dashboard**  
  Displays overall emotion distribution across messages.

---

## Example Encrypted Packet

```json
{
  "emotion_code": "02|03",
  "encrypted_text": "gAAAAAB..."
}
```

Decoded emotions: Sadness, Anger


## Why This Is Interesting

Traditional encryption hides everything.
Mini Emotion Cipher explores a different idea: protect the message, but retain emotional insight.

This can enable:

privacy-aware sentiment analysis

secure mental health monitoring

encrypted communication analytics

## Tech Stack

Python

Streamlit

HuggingFace Transformers

AES Encryption (cryptography)

Deep Translator

Matplotlib
