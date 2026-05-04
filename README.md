# 🤖 JarvisX

A Python-based Jarvis voice assistant that automates desktop tasks, opens apps, and responds to voice commands in real time.

---

## 🚀 Features

- 🎤 Voice command recognition
- 🔊 Text-to-speech response
- 🌐 Open websites (YouTube, Google, ChatGPT)
- 🖥️ Control system (shutdown, screenshot, desktop)
- 📂 Launch desktop applications
- ⚡ Continuous listening mode

---

## 🛠️ Tech Stack

- Python 🐍  
- SpeechRecognition  
- pyttsx3  
- pyautogui  
- webbrowser  
- os  

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Gitanshh20/JarvisX.git
cd JarvisX
```

### 2. Install dependencies
```bash
pip install pyttsx3 SpeechRecognition pyautogui pyaudio
```

> ⚠️ If PyAudio fails:
```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 🎙️ Example Commands

### 🌐 Web Commands
- open youtube  
- open google  
- open chatgpt  
- open my game  

### 🖥️ System Commands
- open desktop  
- take screenshot  
- shutdown  
- new desktop  
- close tab  
- clear terminal  

### 📂 App Commands
- open vs code  
- open discord  
- open github  
- open github desktop  

---

## ⚙️ How It Works

1. Listens to your voice using microphone 🎤  
2. Converts speech to text  
3. Matches command with predefined actions  
4. Executes tasks like opening apps or controlling system  

---

## 📁 Project Structure

```
JarvisX/
│── main.py
│── README.md
```

---

## ⚠️ Notes

- Update app paths according to your system  
- Requires a working microphone  
- Internet required for speech recognition  

---

## 💡 Future Improvements

- Add ChatGPT integration 🤖  
- GUI interface (Tkinter / PyQt)  
- Wake word detection ("Hey Jarvis")  
- More automation features  

---

## 👨‍💻 Author

**Gitansh**  
Aspiring AI Engineer 🚀  
