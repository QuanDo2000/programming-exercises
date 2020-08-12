# http://www.pythonchallenge.com/pc/hex/bin.html

import email
import wave

# Email got from source page
# Start at 'From', end at '==--'
message = open('./resource/email.txt', 'rb').read().decode()

mail = email.message_from_string(message)
# Email is a wav file
audio = mail.get_payload(0).get_payload(decode=True)
# Create .wav audio file
f = open('./output/level19_indian.wav', 'wb')
f.write(audio)
# Audio file has a voice saying 'Sorry'
# Go to page http://www.pythonchallenge.com/pc/hex/sorry.html
# Has content '- "what are you apologizing for?"'

# Map of India, sound file is 'indian.wav'
# Wave sound file is encoded using big or little 'endian' byte orders
# indian.wav is encoded in little-endian

# Open audio file
w = wave.open('./output/level19_indian.wav')
# Result file
h = wave.open('./output/level19_result.wav', 'w')

# Keep channels
h.setnchannels(w.getnchannels())
# Set sampling width to be half
h.setsampwidth(w.getsampwidth() // 2)
# Double the framerate
h.setframerate(w.getframerate() * 2)

# Get frame of original audio
frames = w.readframes(w.getnframes())

# Write new frames to result audio
wave.big_endian = 1
h.writeframes(frames)

# Close files
w.close()
h.close()
# Result audio has 'you are an idiot' song
# Answer: idiot
