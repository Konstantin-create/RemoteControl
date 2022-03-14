def play(message):
    from win32com.client import constants, Dispatch
    Msg = message
    speaker = Dispatch("SAPI.SpVoice")  #Create SAPI SpVoice Object
    speaker.Speak(Msg)                  #Process TTS
    del speaker                         #Delete speaker object and free up memory