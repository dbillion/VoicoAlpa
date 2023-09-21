import openai
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key = api_data

completion = openai.Completion()


def Reply(question):
    prompt = f'Jarvisia🤖 : {question}\n Jarvis: '
    response = completion.create(
        prompt=prompt, engine="text-davinci-003", stop=['\Jarvisia🤖 '], max_tokens=200)
    answer = response.choices[0].text.strip()
    return answer


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello How Are You? ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_gmail(audio, language='en-in')
        print("Jarvisia🤖  Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        ans = Reply(query)
        print(ans)
        speak(ans)
        if 'open twitter' in query:
            webbrowser.open("www.twitter.com")
        if 'open gmail' in query:
            webbrowser.open("www.gmail.com")
        if 'bye' in query:
            break
