#1 - Import the necessary libraries
from TTS.api import TTS
import os

#2: Load the TTS model
model_name = TTS.list_models()[0]  # Use the first available model
tts = TTS(model_name)

#3 - Select the speaker and language
model_name = TTS.list_models()[0]  # Use the first available model
tts = TTS(model_name)

#4 - Set output folder and input text
os.makedirs("output", exist_ok=True)
text = "First, solve the problem. Then, write the code."

#5 Generate the speech and save it to a WAV file
tts.tts_to_file(
    text=text,
    speaker=selected_speaker,  # Provide speaker name
    language=selected_language,  # Provide language code
    file_path="output/output.wav"
)
print("TTS complete! Check the output folder for the audio file.")