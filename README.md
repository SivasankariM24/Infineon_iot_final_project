# Hands-Free Smart Light Control Using Finger Detection and ESP32

A contactless IoT system that controls smart lights using hand gestures detected through computer vision and ESP32 microcontroller.

## 🚀 Features

- **Contactless Control**: Control lights by showing fingers to webcam
- **Real-time Detection**: Instant finger counting using MediaPipe
- **Multiple Light Control**: Control up to 5 different lights
- **Cost-effective**: Uses affordable components (ESP32, webcam)
- **Easy Setup**: Simple USB connection between PC and ESP32

## 🎯 How It Works

1. **Hand Detection**: Webcam captures live video feed
2. **Finger Counting**: MediaPipe processes hand landmarks to count extended fingers
3. **Serial Communication**: Finger count sent to ESP32 via USB
4. **Device Control**: ESP32 controls connected lights based on finger count

## 🔧 Components Required

| Component | Quantity | Description |
|-----------|----------|-------------|
| ESP32 Microcontroller | 1 | Main controller for IoT functionality |
| USB Cable | 1 | Power and serial communication |
| LEDs / Relay Module | 5 | Represents controllable lights |
| Resistors (220Ω) | 5 | Current limiting for LEDs |
| Jumper Wires | ~10 | Circuit connections |
| Webcam | 1 | Video capture for hand detection |
| Computer | 1 | Runs Python detection script |

## 📋 Prerequisites

### Software Requirements
- Python 3.7+
- Arduino IDE
- Git (for cloning)

### Python Libraries
```bash
pip install opencv-python mediapipe pyserial numpy
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SivasankariM24/hands-free-smart-light-control.git
   cd hands-free-smart-light-control
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Upload ESP32 code**
   - Open `esp32_code/light_controller.ino` in Arduino IDE
   - Select your ESP32 board and port
   - Upload the code

4. **Setup hardware connections**
   - Connect LEDs to GPIO pins (2, 4, 5, 18, 19) with resistors
   - Connect ESP32 to computer via USB

## 🎮 Usage

1. **Run the Python script**
   ```bash
   python finger_detection.py
   ```

2. **Show fingers to webcam**
   - 0 fingers: Turn OFF all lights
   - 1 finger: Turn ON Light 1 only
   - 2 fingers: Turn ON Light 2 only
   - 3 fingers: Turn ON Light 3 only
   - 4 fingers: Turn ON Light 4 only
   - 5 fingers: Turn ON Light 5 only

3. **Exit**: Press 'q' to quit the application


## ⚡ Circuit Diagram

```
ESP32 Connections:
GPIO 2  ──[220Ω]── LED1 ── GND
GPIO 4  ──[220Ω]── LED2 ── GND
GPIO 5  ──[220Ω]── LED3 ── GND
GPIO 18 ──[220Ω]── LED4 ── GND
GPIO 19 ──[220Ω]── LED5 ── GND
```

## 🎯 Gesture Mapping

| Fingers Shown | Action |
|---------------|--------|
| 0 | All lights OFF |
| 1 | Light 1 ON (others OFF) |
| 2 | Light 2 ON (others OFF) |
| 3 | Light 3 ON (others OFF) |
| 4 | Light 4 ON (others OFF) |
| 5 | Light 5 ON (others OFF) |

## 🚧 Troubleshooting

### Common Issues

1. **ESP32 not detected**
   - Check USB cable connection
   - Install ESP32 drivers
   - Verify correct COM port in Arduino IDE

2. **Hand detection not working**
   - Ensure good lighting conditions
   - Keep hand clearly visible to webcam
   - Check webcam permissions

3. **Serial communication errors**
   - Verify ESP32 port in Python script
   - Check if ESP32 is already connected to Arduino IDE Serial Monitor
   - Try different baud rates (9600, 115200)

### Performance Tips
- Use good lighting for better hand detection
- Keep hand at appropriate distance from webcam (30-60cm)
- Ensure clear background for better finger detection

## 🔮 Future Enhancements

- [ ] **Wireless Communication**: Replace USB with Wi-Fi/Bluetooth
- [ ] **Voice Control**: Add voice commands as alternative input
- [ ] **Mobile App**: Create smartphone app for remote control
- [ ] **Smart Home Integration**: Connect with Alexa/Google Home
- [ ] **Multiple Gesture Types**: Add swipe gestures, palm detection
- [ ] **Web Dashboard**: Real-time status monitoring interface

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👥 Team Members

**Team Infineon - Madras Institute of Technology,Chennai**
- Akash SJ (2023503048)
- Yuvansankar R (2023503060)
- Rakesh M M (2023503067)
- Sivasankari M (2023503039)
- Abishree S. N (2023503028)
- Sahana M (2023503057)
- Sumitha G K (2023503024)
- Joice Gloriya P (2023503011)
- Pavithra S (2023503046)
- Pradesha P (2023503054)

## 📚 References

- [MediaPipe Documentation](https://mediapipe.dev/)
- [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on GitHub
3. Contact team members

---

**Made by Team Infineon**
