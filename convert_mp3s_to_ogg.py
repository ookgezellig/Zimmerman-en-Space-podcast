import os
from pydub import AudioSegment

# Define the directories for input (MP3) and output (OGG) files
input_dir = 'mp3-files'
output_dir = 'ogg-files'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def convert_mp3_to_ogg(input_file: str, output_file: str) -> None:
    """
    Converts an MP3 file to OGG format.

    Args:
        input_file (str): The path to the input MP3 file.
        output_file (str): The path to the output OGG file.

    Returns:
        None
    """
    try:
        # Load the MP3 file
        audio = AudioSegment.from_mp3(input_file)

        # Export the file in OGG format
        audio.export(output_file, format="ogg")

        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Failed to convert {input_file}: {e}")


# Iterate over all files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.mp3'):
        input_file_path = os.path.join(input_dir, file_name)
        output_file_name = file_name.replace('.mp3', '.ogg')
        output_file_path = os.path.join(output_dir, output_file_name)

        # Convert the MP3 file to OGG
        convert_mp3_to_ogg(input_file_path, output_file_path)

print("Conversion process completed!")
