# Mini Emotion Cipher

> A privacy-preserving messaging system that detects the emotional context of a message while keeping the original content securely encrypted. Built using Transformer-based NLP, AES encryption, and Streamlit.

---

## Overview

Mini Emotion Cipher explores a different approach to secure communication. Instead of treating encryption and emotion analysis as separate tasks, the system combines them by preserving emotional context while protecting the original message.

The application first detects emotions using a Transformer model, encrypts the message using AES encryption, and stores lightweight emotion metadata alongside the encrypted text. This enables privacy-aware analytics without exposing sensitive content.

---

## Features

- Transformer-based emotion detection using DistilRoBERTa
- Multi-emotion classification with confidence scores
- AES encryption for secure message storage
- Emotion metadata encoding
- Emotion-aware decryption
- Multilingual input support
- Emotion prediction caching
- Adaptive user vocabulary learning
- Emotion analytics dashboard

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| NLP | Hugging Face Transformers |
| Emotion Model | DistilRoBERTa |
| Encryption | AES (Cryptography) |
| Translation | Deep Translator |
| Visualization | Matplotlib |

---

## Architecture

```
User Message
      │
      ▼
Language Detection & Translation
      │
      ▼
Emotion Detection (Transformer)
      │
      ▼
Emotion Metadata Encoding
      │
      ▼
AES Encryption
      │
      ▼
Encrypted Emotion Packet
      │
      ▼
Secure Storage / Analytics
      │
      ▼
Message Decryption
```

---

## Live Demo

**Application**

https://mini-emotion-cipher-ish.streamlit.app/

**Demo Video**

https://drive.google.com/drive/folders/1L6kKhELLTQFgQuRr2KPKZEEK-aPKp_B2

---

## Project Structure

```
Mini-Emotion-Cipher/
│
├── app.py
├── encryption/
├── emotion_detection/
├── analytics/
├── utils/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Mini-Emotion-Cipher.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Workflow

1. User enters a message.
2. Language is detected and translated if necessary.
3. The Transformer model predicts the emotional context.
4. Emotion metadata is encoded.
5. The original message is encrypted using AES.
6. An encrypted packet containing the encrypted message and emotion metadata is generated.
7. During decryption, both the original message and emotion information are restored.

---

## Example Output

```json
{
  "emotion_code": "02|03",
  "encrypted_text": "gAAAAAB..."
}
```

Decoded emotions:

- Sadness
- Anger

---

## Applications

- Privacy-preserving communication
- Mental health monitoring
- Secure sentiment analysis
- Communication analytics
- Emotion-aware AI systems

---

## Future Improvements

- End-to-end encrypted messaging
- Cloud database integration
- User authentication
- Mobile application
- Advanced emotion analytics
- Real-time conversations

---

## License

This project is licensed under the MIT License.

---

## Author

**Ishwari**

If you found this project useful, consider giving it a star.
