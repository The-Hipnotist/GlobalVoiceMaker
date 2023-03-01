# GlobalVoiceMaker
Automatically makes a voice for any AI voice program or site, made in Python. This was originally made for voice.ai, but can be used for any AI site.

## Requirements:
1. `pip install requirements.txt`
2. FFmpeg
3. YouTube URL
4. There is no step 4

### Some things to know:
1. You **cannot** use the same name twice for the output files. For example, if you name the output file "lilyvtube", you **cannot** use "lilyvtube" again, otherwise file conflicts will happen. **However**, you can put any other character either in front, in between, or at the end of the name (for example, "lilyvtube2" or "6lilyvtube", etc) and everything will work fine.
2. You **will** have to run the script again for multiple videos/audio.
3. To get ffmpeg to work globally, both for this script and in general, download ffmpeg from [here](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip), then move the **extracted** ffmpeg folder to your C: drive, rename it to **just** ffmpeg, then go into your system environment variable settings, double click path, click add, then add the path where it is installed in your C: drive (it should be C:\ffmpeg\bin) to both your user variables and your system variables. **If you have any cmd or powershell windows open, close them for the new path to take effect.** Now, if you open a cmd or powershell window and type `ffmpeg`, it should print it.
