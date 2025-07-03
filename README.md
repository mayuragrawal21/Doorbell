
# 🔔 Smart Door Entry Bell

A Raspberry Pi-powered **Smart Door Entry System** that captures an image using a camera module whenever the doorbell is pressed and instantly sends the image to the property owner's **Telegram** account for real-time visitor notifications.

## 🏫 Project Affiliation

Developed as part of an IoT & Computer Vision project at  
**Ajeenkya D Y Patil University**

## 🚀 Features

- 📸 **Live Image Capture** via OpenCV on doorbell press
- 📲 **Instant Image Notification** to the owner using Telegram Bot API
- 🍓 **Built on Raspberry Pi** for compact, real-world deployment
- 🔌 Can be extended to include face recognition, speaker/mic integration, or cloud-based access logging

## 🗂️ File

- `door_bell.py`: Core script that handles GPIO input, captures image, and sends it to Telegram.

## 🛠️ Requirements

- Raspberry Pi with Camera Module
- Python 3
- OpenCV
- Telegram Bot API token and chat ID
- GPIO library (for button press detection)

### 📦 Install Required Packages

```bash
pip install opencv-python requests RPi.GPIO
```

### ⚙️ Telegram Setup

1. Create a bot using [BotFather](https://t.me/botfather) on Telegram.
2. Get your **Bot Token** and **Chat ID**.
3. Add them to `door_bell.py` in the respective placeholders.

### ▶️ Run

```bash
python door_bell.py
```

Pressing the doorbell button will trigger the script to capture and send a photo.

## 🌐 Applications

- Smart homes
- Visitor monitoring
- Contactless access notification systems
- Senior safety and assisted living homes

## 👤 Author

**Mayur Agrawal**  
🔗 [GitHub](https://github.com/mayuragrawal21) | [LinkedIn](https://www.linkedin.com/in/mayur-agrawal21/)  
📧 [agrawalmayur2001@gmail.com](mailto:agrawalmayur2001@gmail.com)

---

> ⚠️ For demo, academic, or prototype use only. Hardware reliability and security measures should be considered for real deployments.
