# Zimmerman en Space go Wiki
Webscrape of the [Zimmerman en Space podcast](https://www.buzzsprout.com/2096278), and (re)publication on Wikimedia Commons. High 5 for CC0 licenses!

![afbeelding](https://github.com/user-attachments/assets/80910b8e-0c9c-4df1-a3a3-1dc60e1fa426)


## Step by step process

### Make initial scrape map 
* Zimmerman en Space podcast URL list, Season 1, Episodes 1 to 92 : [https://ookgezellig.github.io/Zimmerman-en-Space-podcast/episodes.html](https://ookgezellig.github.io/Zimmerman-en-Space-podcast/episodes.html)
* To be used as initial scrape map by [webscraper.oi](https://webscraper.io/) for scraping data of individual episodes

### Excel with scraped data, post-processing
Output of webscrape, with post-processing to make data suitable for Wikimedia commons and OpenRefine: [https://ookgezellig.github.io/Zimmerman-en-Space-podcast/ZimmermanEnSpacePodcast_episodes1-92.xlsx](ZimmermanEnSpacePodcast_episodes1-92.xlsx)

### Download mp3s from URL
* Python script: [download_mp3s.py](download_mp3s.py)
* Folder: [mp3-files](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/tree/main/mp3-files)
* Filenames are Buzzsprout titles, eg. [11845039-tsunami-s-op-mars.mp3](mp3-files/11845039-tsunami-s-op-mars.mp3)

### Convert .mp3 to .ogg, a format suitable for Wikimedia Commons
* Python script: [convert_mp3s_to_ogg.py](convert_mp3s_to_ogg.py) - Make sure [ffmpeg](https://ffmpeg.org/download.html) 
  is installed on your machine and it has been added to your System's PATH.
* Alternatively, use an online .mp3 to .ogg bulk converter, such as [online-audio-converter.com](https://online-audio-converter.com/) 
* Folder: [ogg-files](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/tree/main/ogg-files) - files 1-92
* Files have been renamed from Buzzsprout titles to Wikimedia Commons titles, eg. [File:Tsunami's_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.ogg](ogg-files/Tsunami's_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.ogg)

### Input for OpenRefine
* Excel file as source for OpenRefine project, to bulk upload .ogg files and metadata to Wikimedia Commons: see Excel above, this includes all columns needed for the OpenRefine project.
* OpenRefine project files : [xxx.tar.gz]]()
* 
### Upload to Wikimedia Commons
* [Category:Zimmerman_en_Space_podcast](https://commons.wikimedia.org/wiki/Category:Zimmerman_en_Space_podcast)
* Hens Zimmerman Wikidata item : https://www.wikidata.org/wiki/Q130279350 

## Copyright 
= CC0
