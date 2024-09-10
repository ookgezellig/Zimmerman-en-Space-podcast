import os
import pandas as pd
import requests
from typing import Optional

# Load the Excel file
file_path: str = 'ZimmermanEnSpacePodcast_episodes1-92.xlsx'
data: pd.DataFrame = pd.read_excel(file_path)

# Extract the 'episode mp3 url' column
mp3_urls: pd.Series = data['episode mp3 url']

# Create a directory for saving MP3 files if it doesn't exist
output_dir: str = 'mp3-files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def download_mp3(url: str, folder: str) -> Optional[str]:
    """
    Downloads an MP3 file from the given URL and saves it in the specified folder.

    Args:
        url (str): The direct URL to the MP3 file.
        folder (str): The path to the folder where the MP3 file will be saved.

    Returns:
        Optional[str]: The name of the file if the download was successful, None otherwise.

    Raises:
        requests.exceptions.RequestException: If there's an issue with the HTTP request.
    """
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/58.0.3029.110 Safari/537.36')
    }

    try:
        response: requests.Response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract file name from the URL
        file_name: str = url.split('/')[-1]
        file_path: str = os.path.join(folder, file_name)

        # Write the mp3 file to disk
        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded: {file_name}")
        return file_name

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - URL: {url}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error downloading {url}: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

# Download all mp3 files
for url in mp3_urls:
    if pd.notnull(url):
        download_mp3(url, output_dir)

print("Download process completed!")
