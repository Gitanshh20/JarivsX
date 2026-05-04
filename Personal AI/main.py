import os
import pyautogui
import pyttsx3
import webbrowser as wb
import speech_recognition as sr 

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

engine.setProperty('rate', 150) 
engine.setProperty('volume', 1) 

def take_command():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        instruction = r.recognize_google(audio)
        print("You:", instruction)

        return instruction.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""

    instruction = instruction.lower().strip()

speak("Hi I am Jarvis What can I help you?")
  
def all_Command():

    while True:

        instruction = take_command()
        
        if "exit" in instruction:
            return False

        # Web Command https://

        def Web_command():

                if "open youtube" in instruction:
                    wb.open("https://youtube.com")
                
                elif "open google" in instruction:
                    wb.open("https://google.com")

                elif "open chatgpt" in instruction:
                    wb.open("https://chatgpt.com/")

                elif "open my game" in instruction:
                    wb.open("https://poki.com/en/g/little-master-cricket")

        Web_command()

        # KeyBorad Command 


        def Key_Command():

                if "open desktop" in instruction:
                    pyautogui.hotkey('win', 'd')

                elif "take screenshot" in instruction:
                    pyautogui.hotkey('win','shift','s')

                elif "shutdown" in instruction:
                    os.system("shutdown /s /t 0")

                elif "new desktop" in instruction:
                    pyautogui.hotkey('win','tab')

                elif "close tab" in instruction:          
                    pyautogui.hotkey('alt','F4')

                elif "clear terminal" in instruction:
                    os.system('cls' if os.name == 'nt' else 'clear')

        Key_Command()

        # Desktop App Command

        def Install_App():

                if "open vs code" in instruction:
                    os.system('"C:\\Users\\OM Computer\\OneDrive\\Desktop\\Visual Studio Code.lnk"')

                elif "open discord" in instruction:
                    os.system('"C:\\Users\\OM Computer\\OneDrive\\Desktop\\Discord.lnk"')

                elif "open github" in instruction:
                    os.system('"C:\\Users\\OM Computer\\OneDrive\\Desktop\\GitHub.lnk"')

                elif "open github desktop" in instruction:
                    os.system('"C:\\Users\\OM Computer\\OneDrive\\Desktop\\GitHub Desktop.lnk"')

        Install_App()

all_Command()