from pydub import AudioSegment
import simpleaudio as sa
import os
import random

AudioSegment.ffmpeg = "D:\\ffmpeg\\bin\\ffmpeg.exe"

music_directory = 'D:\\projetos\\PythonChatBot\\PythonChatBot\\music'

music_files = [os.path.join(music_directory, f) for f in os.listdir(music_directory) if f.endswith('.mp3')]

random_music = random.choice(music_files)

song = AudioSegment.from_mp3(random_music)

play_obj = sa.play_buffer(song.raw_data, num_channels=song.channels, bytes_per_sample=song.sample_width, sample_rate=song.frame_rate)

play_obj.wait_done()

