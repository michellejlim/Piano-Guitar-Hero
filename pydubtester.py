import module_manager
module_manager.review()

from glob import glob
import pyaudio
import wave

import pydub

from pydub import AudioSegment

song = AudioSegment.from_wav("sounds/D1.wav")
newsong = song+song
newsong.export("mash.wav",format="wav")

def play(file):
    CHUNK = 1024 #measured in bytes

    wf = wave.open(file, 'rb')
    
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    stream.stop_stream()
    stream.close()

    p.terminate()