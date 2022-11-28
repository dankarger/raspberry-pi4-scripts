import speech_recognition as sr

listening = True

while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000
        
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5.0)
            print(recognizer)
            response = recognizer.recognize_sphinx(audio)
            print(response)
        except sr.UnknownValueError:
            print("Didn't recognize that")
            
                
