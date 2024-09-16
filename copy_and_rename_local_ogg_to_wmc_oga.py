import os
import shutil
import pandas as pd
def copy_and_rename_ogg_files(input_folder_path, excel_file, sheet_name, output_folder_path):

    """
    Rename and copy all .ogg files in a
       * FROM Buzzsprout syntax, eg. "ogg-files/11845039-tsunami-s-op-mars.ogg"
       * TO Wikimedia Commons target syntax eg. "oga-files/Tsunami's_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.oga"
    using data in columns in an Excel file.

    - Input folder to read files from = "ogg-files"
    - Output folder to write renamed files to = "oga-files"

    - Info about the Excel file, its sheet ,and its colums:
        * Excel file name = "ZimmermanEnSpacePodcast_episodes1-92.xlsx"
        * Sheetnname = "episodes"
        * Relevant columns in sheet :
           - Original files names are in the column "LocalOggFileName". Example: "11845039-tsunami-s-op-mars.ogg"
           - Target Wikimedia Commons file names are in the column "WikiCommonsOggFileName". Example:  "Tsunami's_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.oga"
           - Datestamp (example "2022-12-09") of the target file in YYYY-MM-DD syntax is created from the columns "YearYYYY", "MonthNumerical" and "DayDD"
           - Title of the target file  (example: "Tsunami's_op_Mars") is created from the columns "episodeTitle"
           - "_-_Zimmerman_en_Space_-_" is a default string for all target file titles
           - The part "S01E01" in the target file title stand for "Season01, Episode 01" where the Seasons number (example:"01") is stored in the column "season" and the episode number (example: "01") is stored in the column named "episode"
           * The BuzzsproutID (example : "11845039") from the original file name can be reused in the target file name

    :param input_folder_path: Folder path where the .ogg files are located
    :param excel_file: Path to the Excel file containing the renaming data.
    :param sheet_name: Name of the sheet in the Excel file that contains the renaming data.
    :param output_folder_path: Folder path where the renamed .oga files will be saved.
    """

    # Load Excel file and sheet
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Ensure input folder exists
    if not os.path.exists(input_folder_path):
        print(f"Folder '{input_folder_path}' does not exist.")
        return

    # Ensure output folder exists
    if not os.path.exists(output_folder_path):
        print(f"Folder '{output_folder_path}' does not exist.")
        return

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Extract relevant information from the DataFrame
        original_file_name = row['LocalOggFileName']
        target_file_name = row['WikiCommonsOgaFileName']
        buzzsprout_id = original_file_name.split('-')[0]
        season_number = f"{int(row['season']):02d}"
        episode_number = f"{int(row['episode']):02d}"

        # Create target file name
        date_stamp = f"{row['YearYYYY']}-{row['MonthNumerical']:02d}-{row['DayDD']:02d}"
        title = row['episodeTitleForCommons']
        default_string = "_-_Zimmerman_en_Space_-_"
        new_file_name = f"{title.replace(' ', '_')}{default_string}S{season_number}E{episode_number}_-_{date_stamp}_-_{buzzsprout_id}.oga"

        # Full paths for the original and new file names
        original_file_path = os.path.join(input_folder_path, original_file_name)
        new_file_path = os.path.join(output_folder_path, new_file_name)

        # Copy and rename the file if it exists
        if os.path.isfile(original_file_path):
            shutil.copy2(original_file_path, new_file_path)
            print(f"Copied and renamed '{original_file_name}' to '{new_file_name}'.")
        else:
            print(f"File '{original_file_name}' does not exist in '{input_folder_path}'.")


if __name__ == "__main__":
    excel_file = "ZimmermanEnSpacePodcast_episodes1-92.xlsx"
    sheet_name = "episodes"
    input_folder_path = "ogg-files"
    output_folder_path = "oga-files"
    copy_and_rename_ogg_files(input_folder_path, excel_file, sheet_name, output_folder_path)
