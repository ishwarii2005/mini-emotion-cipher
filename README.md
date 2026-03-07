# Mini Emotion Cipher

Mini Emotion Cipher is a privacy-preserving emotion analysis system that detects emotional context in user messages while keeping the actual text encrypted.

## Features
- Transformer-based emotion detection
- Multi-emotion analysis
- Multilingual support
- AES encryption for message privacy
- Emotion metadata preservation
- Emotion analytics dashboard
- Emotion caching for faster processing
- Adaptive vocabulary learning

## How it Works
1. User inputs a message
2. Language detection + translation (if needed)
3. Emotion detection using DistilRoBERTa
4. Top emotions encoded as metadata
5. Message encrypted using AES
6. Emotional signature preserved for analysis
