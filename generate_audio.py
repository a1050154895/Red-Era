import wave
import math
import struct
import os

# Configuration
AUDIO_DIR = "RedEra/game/audio"
MUSIC_DIR = os.path.join(AUDIO_DIR, "music")
SFX_DIR = os.path.join(AUDIO_DIR, "sfx")

os.makedirs(MUSIC_DIR, exist_ok=True)
os.makedirs(SFX_DIR, exist_ok=True)

def generate_tone(filename, duration=1.0, freq=440.0, vol=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * duration)
    
    with wave.open(filename, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sample_rate)
        
        for i in range(n_samples):
            # Generate sine wave
            value = int(32767.0 * vol * math.sin(2.0 * math.pi * freq * i / sample_rate))
            data = struct.pack('<h', value)
            w.writeframes(data)
    
    print(f"Generated: {filename}")

# Music Placeholders (Longer, lower freq)
music_files = {
    "history_epic.wav": 220.0,
    "history_sad.wav": 180.0,
    "history_tension.wav": 300.0,
    "blue_cyber.wav": 440.0, # Higher pitch for cyber
    "blue_glitch.wav": 880.0,
    "red_march.wav": 110.0, # Low march
    "red_space.wav": 500.0,
}

for name, freq in music_files.items():
    # Make them short loops (5 seconds) to save space but audible
    generate_tone(os.path.join(MUSIC_DIR, name), duration=5.0, freq=freq, vol=0.3)

# SFX Placeholders (Short, high freq)
sfx_files = {
    "typewriter.wav": 1000.0,
    "explosion.wav": 100.0, # Low boom
    "rain.wav": 800.0, # Noise is hard, just a tone for now
    "glitch.wav": 2000.0,
    "crowd.wav": 400.0,
}

for name, freq in sfx_files.items():
    generate_tone(os.path.join(SFX_DIR, name), duration=0.5, freq=freq, vol=0.5)
