from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

model = Model(r"/home/pi/Desktop/speech/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
engine = pyttsx3.init()

listening = False

def get_command():
    listening = True
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    while listening:
        stream.start_stream()
        try:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(result)
                response = result[14:-3]
                listening = False
                stream.close()
                return response
        except OSError:
            pass
        
while True:
    print("Waiting for command...")
    command = get_command()
    if command =="":
        print('ii')
        pass
    elif command == "hello":
        engine.say("Hello")
        print('hhhelllo')
        engine.runAndWait()
    elif command == "make coffee" or command=='please make coffee' or command=='make coffee please':
        engine.say("Ok, making coffee")
        print('j')
        engine.runAndWait()
    elif command == "thanks" or command=='thank you':
        engine.say("You welcome")
        print('j')
        engine.runAndWait()
    elif command == "how are you" or command == "how our you" :
        engine.say("I am good, thanks")
        print('jhhhh')
        engine.runAndWait()
    else:
        engine.say("I dont understand")
        print('dont')
        engine.runAndWait()
        
#    if key == 27:   #ESC
 #       break


