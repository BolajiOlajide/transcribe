import speech_recognition as sr


def audio_transcribe(AUDIO_FILE):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "Error: Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        error_message = (
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
        print(error_message)
        return error_message
