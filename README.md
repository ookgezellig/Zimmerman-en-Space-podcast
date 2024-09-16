# Zimmerman en Space go Wiki
Webscrape of the [Zimmerman en Space](https://www.buzzsprout.com/2096278) podcast, and (re)publication on Wikimedia Commons (and Zenodo in the future). High 5 for CC0 licenses, space, astronomy and nerds!

![afbeelding](https://github.com/user-attachments/assets/80910b8e-0c9c-4df1-a3a3-1dc60e1fa426)

## Step by step process
*Latest update* : 16 September 2024

### Make initial scrape map 
* *Zimmerman en Space* podcast URL list, Season 1, Episodes 1 to 92 : [https://ookgezellig.github.io/Zimmerman-en-Space-podcast/episodes.html](https://ookgezellig.github.io/Zimmerman-en-Space-podcast/episodes.html)
* To be used as initial scrape map by [webscraper.oi](https://webscraper.io/) for scraping data of individual episodes

### Excel with scraped data, post-processing
Output of webscrape, with post-processing to make data suitable input for Wikimedia Commons, OpenRefine and the Python modules used below: [https://ookgezellig.github.io/Zimmerman-en-Space-podcast/ZimmermanEnSpacePodcast_episodes1-92.xlsx](ZimmermanEnSpacePodcast_episodes1-92.xlsx)

### Download mp3s from URL
* Python script: [download_mp3s.py](download_mp3s.py)
* Folder: [mp3-files](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/tree/main/mp3-files)
* Filenames are Buzzsprout titles, eg. [11845039-tsunami-s-op-mars.mp3](mp3-files/11845039-tsunami-s-op-mars.mp3)

### Convert .mp3 to .oga, a format suitable for Wikimedia Commons

Converting from mp3 to ogg/oga:
* Python script: [convert_mp3s_to_oga.py](convert_mp3s_to_oga.py) - Make sure [ffmpeg](https://ffmpeg.org/download.html) 
  is installed on your machine and it has been added to your System's PATH.
* Alternatively, use an online .mp3 to .ogg bulk converter, such as [online-audio-converter.com](https://online-audio-converter.com/). This was the actual tool used for converting the first batch of episodes (1-92). File extension can be changed from .ogg tot .oga without penalty.
* Folder: [ogg-files](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/tree/main/ogg-files) 

Wikimedia Commons:
* Files must be copied and renamed from Buzzsprout to Wikimedia Commons syntax titles, eg. from [ogg-files/11845039-tsunami-s-op-mars.ogg](ogg-files/11845039-tsunami-s-op-mars.ogg) to [oga-files/Tsunami's_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.oga](oga-files/Tsunami's_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.oga)
   * Python script: [copy_and_rename_local_ogg_to_wmc_oga.py](copy_and_rename_local_ogg_to_wmc_oga.py)
* Folder with Commons compatible files: [oga-files](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/tree/main/oga-files) 

### Input for OpenRefine
* Excel file as source for OpenRefine project, to bulk upload the .oga files and metadata to Wikimedia Commons: see Excel above, this includes all columns needed for the OpenRefine project.
* OpenRefine project files : [ZimmermanEnSpacePodcast-episodes1-92-xlsx.openrefine.tar.gz](ZimmermanEnSpacePodcast-episodes1-92-xlsx.openrefine.tar.gz)


### Wikimedia Commons
#### Category
* [Category:Zimmerman en Space podcast](https://commons.wikimedia.org/wiki/Category:Zimmerman_en_Space_podcast)

#### SPARQL 
Structured data has been added to all files, so we can do some (basic) semantic searching via SPARQL queries.
* [All episodes, sorted by year](https://w.wiki/BDH9)
* [All episodes about Mars]() - to do

### Wikidata
* Hens Zimmerman Wikidata item : https://www.wikidata.org/wiki/Q130279350 



## Copyright 
All episodes 1-92 of the *Zimmerman en Space* podcast have been licensed under the [Creative Commons CC0 1.0 license](http://creativecommons.org/publicdomain/zero/1.0), as stated in the shownotes of each episode.
