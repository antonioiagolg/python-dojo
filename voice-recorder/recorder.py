'''
Simple audio recorder.
For this I created an virtual environment and
I installed sounddevice and wavio package.

References:
- https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/

'''

import sounddevice as sd
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration in seconds
duration = 5


# Starting the recording
# In my case, my microphone is an device audio which is not the default
# so I had to run python3 -m sounddevice to list all the device resources
# and I found my mic as the index 10. Them I was able to record. For my mic,
# sounddevice was not able to find the proper number of channels. Setting 1
# was good enough.
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1, device=10)

# Record the audio until the number of seconds
sd.wait()

# Saving the audio array
wv.write("recording1.wav", recording, freq, sampwidth=2)
