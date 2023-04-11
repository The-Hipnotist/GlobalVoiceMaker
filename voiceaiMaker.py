import os, shutil, wave, auditok, glob, random, time, warnings, yt_dlp, glob, traceback
warnings.filterwarnings("ignore")
if os.path.isdir("splitaudio"):
    shutil.rmtree("splitaudio")
ytinput = input("Enter a youtube url here: ")
try:
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    }
    print(f"Downloading video...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytinput])
    for file in glob.glob("*.wav"):
        if os.path.exists(file):
            os.rename(file, "mono.wav")
except:
    print("An error has happened.")
    print(traceback.format_exc())
    time.sleep(2)
    exit(0)

print("Done.")
time.sleep(0.5)
os.system("cls")
foldername = "wavs"
folderpath = f'{foldername}/';
folderpath2 = 'converted/';
if os.path.exists(foldername):
    print("Wavs folder already exists!")
else:
    os.mkdir(foldername)
    shutil.move("mono.wav", "wavs/")
    os.system("cls")
    name = input("Enter a name for the output files: ")
    print("Name set as " + name)
    time.sleep(0.5)
    os.system("cls")
    os.mkdir(folderpath2)
    os.rename("wavs/mono.wav", "converted/mono.wav")
    os.rmdir("wavs")
    if os.path.exists("splitaudio"):
        pass
    else:
        os.mkdir("splitaudio")
    shutil.move("converted/mono.wav", "splitaudio/mono.wav")
    os.rmdir("converted")
    time.sleep(1)
    os.system("cls")
    maxdurcutoff = int(input("Enter a max duration for cutoff, or press '0' for default (10): "))
    if maxdurcutoff == 0:
        maxdurcutoff = 10
    audioregions = auditok.split(
        "splitaudio/mono.wav",
        min_dur=1,
        max_dur=maxdurcutoff,
        max_silence=0.3,
        energy_threshold=45,
    )
    for i, r in enumerate(audioregions):
        filename = r.save("Region_{meta.start:3f}-{meta.end:.3f}.wav")
    for f in sorted(glob.glob("*.wav")):
        newname = name + "-" + str(random.randint(1, 910719)) + ".wav"
        os.rename(f, newname)
    os.remove("splitaudio/mono.wav")
    for o in glob.glob(f"{name}-*.wav"):
        shutil.move(o, "splitaudio")
    filecount = len([f for f in os.listdir('splitaudio')if os.path.isfile(os.path.join('splitaudio', f))])
    totalminutes = 0
    for f in glob.glob("splitaudio/*.wav"):
        with wave.open(f, 'rb') as wave_file:
            framerate = wave_file.getframerate()
            frames = wave_file.getnframes()
            duration = frames / float(framerate)
            totalminutes = totalminutes + duration
    totalminutes = round(totalminutes / 60, 1)
    print(f"Done! {filecount} files in the folder, {totalminutes} minutes of audio total.")
    if totalminutes > 15.0:
        print("There are enough audio files to train a voice now!")
        time.sleep(3)
    else:
        print(f"You need {round(15.0 - totalminutes, 1)} more minutes of audio to train a voice.")
        time.sleep(3)
