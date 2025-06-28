import speech_recognition as sr
import webbrowser
import pyttsx3
import music

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        speak("Initial Jarvis")
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            text = r.recognize_google(audio)
            print(f"You said: {text}")
            text_lower=text.lower()
            if any (stop_words in text_lower for stop_words in ["stop", "exit", "quit", "close", "bye", "goodbye"]):
                speak("Goodbye Zeeshan ! Have a great day!")
                break
            website = text.lower().replace("open", "").strip()

            if "google" in website:
                url = "https://www.google.com"
            elif "youtube" in website:
                url = "https://www.youtube.com"
            elif "facebook" in website:
                url = "https://www.facebook.com"
            elif "twitter" in website:
                url = "https://www.twitter.com"
            elif "instagram" in website:
                url = "https://www.instagram.com"
            elif "linkedin" in website:
                url = "https://www.linkedin.com"
            elif "github" in website:
                url = "https://www.github.com"
            elif text.lower().startswith("play music"):
                parts = text.lower().split(" ")
                if len(parts) > 2:
                    song = parts[2]  # if you say "play music one"
                elif len(parts) > 1:
                    song = parts[1]  # if you say "play music"
                else:
                    song = ""

                link = music.musics.get(song)
                if link:
                    webbrowser.open(link)
                    speak(f"Playing {song} music")
                    continue
                else:
                    speak("Sorry, I didn't recognize that music.")
                    continue
            elif "open" in text.lower():
                if website.startswith("www."):
                    url = f"https://{website}"
                else:
                    url = f"https://{website}.com"
            else:
                speak("I can only open websites. Please say 'open' followed by the website name.")
                continue

            webbrowser.open(url)
            speak(f"Opening {website}")

        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.WaitTimeoutError:
            print("Timeout error. You were silent.")
            speak("You stayed silent. Try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("Could not request results.")
        except Exception as e:
            print(f"Error: {e}")
            speak("Something went wrong.")
