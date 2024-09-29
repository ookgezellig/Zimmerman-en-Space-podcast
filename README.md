# Zimmerman en Space go Wiki
Webscrape of the [Zimmerman en Space](https://zimmerman-en-space.buzzsprout.com/) podcast, and (re)publication on Wikimedia Commons (and Zenodo in the future). High 5 for CC0 licenses, space, astronomy and nerds!

*Latest update* : 17 September 2024

![afbeelding](images/Zimmerman_en_Space_podcast_logo1.png)

##  Main result
Episodes 1 - 92 are now available on Wikimedia Commons: 
* Category: [Zimmerman en Space podcast](https://commons.wikimedia.org/wiki/Category:Zimmerman_en_Space_podcast)
* Gallery, grouped by year, sorted by date : [Zimmerman en Space podcast](https://commons.wikimedia.org/wiki/Zimmerman_en_Space_podcast)

-----------------------

## Step by step process

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
#### Category & gallery
* Category: [Zimmerman en Space podcast](https://commons.wikimedia.org/wiki/Category:Zimmerman_en_Space_podcast)
* Gallery, grouped by year, sorted by date : [Zimmerman en Space podcast](https://commons.wikimedia.org/wiki/Zimmerman_en_Space_podcast)
* Category: [Hens Zimmerman](https://commons.wikimedia.org/wiki/Category:Hens_Zimmerman)

#### Stuff in progress

##### 1 - Audio transcriptions
Full-text audio transcriptions are being added bit by bit to the Commons files in the coming months. For current status, see [this issue](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/issues/2). 

For a fully worked example, see S01E01 [Tsunami's op Mars](https://commons.wikimedia.org/wiki/File:Tsunami%27s_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.oga#%7B%7Bint%3Afiledesc%7D%7D)

##### 2 - Structured file data / main subject
To the structured data of each Commons file, [main subject (P921)](https://www.wikidata.org/wiki/Special:EntityPage/P921) will be added bit by bit in the coming months. These episode subjects/keywords will be extracted from the title and full-text audio transcriptions using Named Entity Recognition (NER) techniques and subsequent reconciliation of the found entities against Wikidata.
For current status, see [this issue](https://github.com/ookgezellig/Zimmerman-en-Space-podcast/issues/1).

For a fully worked example, see S01E01 [Tsunami's op Mars](https://commons.wikimedia.org/wiki/File:Tsunami%27s_op_Mars_-_Zimmerman_en_Space_-_S01E01_-_2022-12-09_-_11845039.oga#%7B%7Bint%3Afiledesc%7D%7D)

#### API
* [Request info about all episodes, as JSON](https://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmlimit=max&gcmtitle=Category:Zimmerman%20en%20Space%20podcast&prop=info&gcmtype=file)

Request info about episode 14, [AI en Chat GPT in de sterrenkunde](https://commons.wikimedia.org/wiki/File:AI_en_Chat_GPT_in_de_sterrenkunde_-_Zimmerman_en_Space_-_S01E14_-_2023-03-07_-_12392457.oga) 
* [Structured data, as JSON](https://commons.wikimedia.org/w/api.php?action=wbgetentities&format=json&ids=M152723347)
* [Wikitext, as XML](https://magnus-toolserver.toolforge.org/commonsapi.php?image=File:AI%20en%20Chat%20GPT%20in%20de%20sterrenkunde%20-%20Zimmerman%20en%20Space%20-%20S01E14%20-%202023-03-07%20-%2012392457.oga&meta&format=xml)

#### SPARQL 
Structured data has been added to all files, so we can do some (basic) semantic searching via SPARQL queries.
* [All episodes, sorted by year](https://w.wiki/BDH9)
* [All episodes about Mars]() - to do

### Wikidata
* Zimmerman en Space podcast: [https://www.wikidata.org/wiki/Q130355362](https://www.wikidata.org/wiki/Q130355362)
* Hens Zimmerman : [https://www.wikidata.org/wiki/Q130279350](https://www.wikidata.org/wiki/Q130279350) 


-----------------------------

## Copyright 
All episodes 1-92 of the *Zimmerman en Space* podcast have been licensed under the [Creative Commons CC0 1.0 license](http://creativecommons.org/publicdomain/zero/1.0), as stated in the shownotes of each episode.
