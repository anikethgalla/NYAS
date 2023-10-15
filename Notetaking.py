from datetime import datetime
import speech_recognition as sr
from logging.config import listen
import pyttsx3
#speech engine intiallisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voices = engine.getProperty('voices')
for voice in voices:#chnage to female voice
    if "Zira" in voice.name:
        engine.setProperty('voice', voice.id)
activationWord = 'computer' #always should be a single word
def speak(text, rate = 175):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
    
def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech... ')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query
if __name__ =='__main__':
    speak('All systems nominal.', 120)

    while True:
        #parse as list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)


            #note taking
            if query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(now)
                    newFile.write(' ')
                    newFile.write(newNote)
                    speak('Note written')