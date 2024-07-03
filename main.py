# main.py

import os
from moviepy.editor import VideoFileClip
import whisper

# Set the paths
video_folder = "videos"
video_filename = "example_video.mp4"  # Replace with your actual video file name
video_path = os.path.join(video_folder, video_filename)

audio_folder = "audios"
output_audio_path = os.path.join(audio_folder, "temp_audio.mp3")

# Extract audio from the video
video = VideoFileClip(video_path)
video.audio.write_audiofile(output_audio_path)

# Load the Whisper ASR model / select from tiny,base,small,medium,large
model = whisper.load_model("large")

# Transcribe the extracted audio
result = model.transcribe(output_audio_path)
print(result["text"])

# Save the transcription to a text file
transcription_folder = "transcriptions"
output_text_path = os.path.join(transcription_folder, "transcription.txt")

with open(output_text_path, "w") as f:
    f.write(result["text"])

# Remove the temporary audio file
os.remove(output_audio_path)
