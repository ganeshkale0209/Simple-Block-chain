from flask import Flask, render_template, request
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Initialize Speech Recognition
recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assistant', methods=['POST'])
def assistant():
    if request.method == 'POST':
        text = request.form['user_input']
        response = get_assistant_response(text)
        return render_template('index.html', response=response)

def get_assistant_response(text):
    try:
        # Convert text to speech
        engine.say(text)
        engine.runAndWait()
        # Convert speech to text
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)

if __name__ == '__main__':
    app.run(debug=True)
