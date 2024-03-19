import os

os.system("pip install sox")

import sox

import subprocess

# Get all audio files in the current directory
audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]

# Loop through the audio files and apply audio compression
for audio_file in audio_files:
    # Create a new file name for the compressed audio
    compressed_file = audio_file.replace('.wav', '_compressed.wav')

    # Apply audio compression using Sox
    subprocess.call(['sox', audio_file, compressed_file, 'compand 0.6,1,-60,-40,-1'])

# softy_plug