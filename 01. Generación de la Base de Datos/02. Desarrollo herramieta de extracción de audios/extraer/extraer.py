import argparse as agp
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.silence import split_on_silence
from os import path


parser = agp.ArgumentParser()
parser.add_argument("--path", "-p", help="set path")
args = parser.parse_args()

if args.path:
    print(args.path)
"""
video = mp.VideoFileClip(r"C:/Users/domer/OneDrive/UPS/ERASMUS/EduTech/01. Generación de la Base de Datos/02. Desarrollo herramieta de estracción de audios/extraer/video.mp4")
video.audio.write_audiofile(r"C:/Users/domer/OneDrive/UPS/ERASMUS/EduTech/01. Generación de la Base de Datos/02. Desarrollo herramieta de estracción de audios/extraer/resultado.wav")

#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")

audio = AudioSegment.from_wav("C:/Users/domer/OneDrive/UPS/ERASMUS/EduTech/01. Generación de la Base de Datos/02. Desarrollo herramieta de estracción de audios/extraer/resultado.wav")

def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

# Load your audio.
#song = AudioSegment.from_mp3("../resultado.mp3")

# Split track where the silence is 2 seconds or more and get chunks using 
# the imported function.
chunks = split_on_silence (
    # Use the loaded audio.
    audio, 
    # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
    min_silence_len = 1000,
    # Consider a chunk silent if it's quieter than -16 dBFS.
    # (You may want to adjust this parameter.)
    silence_thresh = -32
)


# Process each chunk with your parameters
for i, chunk in enumerate(chunks):
    # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
    silence_chunk = AudioSegment.silent(duration=1000)

    # Add the padding chunk to beginning and end of the entire chunk.
    audio_chunk = silence_chunk + chunk + silence_chunk

    # Normalize the entire chunk.
    normalized_chunk = match_target_amplitude(audio_chunk, -20.0)

    # Export the audio chunk with new bitrate.
    print("Exporting chunk{0}.mp3.".format(i))
    normalized_chunk.export(
        ".//chunk{0}.mp3".format(i),
        bitrate = "192k",
        format = "mp3"
    )
"""