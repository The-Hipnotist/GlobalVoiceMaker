from pytube import YouTube, exceptions
import os, shutil, wave, auditok, glob, random, subprocess, time, warnings
warnings.filterwarnings("ignore")
ytinput = input("Enter a youtube url here: ")
try:
    yt = YouTube(ytinput)
    print(f"Downloading video ['{yt.title}'] by ['{yt.author}']...")
except exceptions.RegexMatchError:
    print("That is not a valid URL! Please try again!")
    time.sleep(2)
    exit(0)
if os.path.exists("audio.3gpp"):
    time.sleep(0.50)
    print("audio.3ggp file detected, removing...")
    os.remove("audio.3gpp")
video = yt.streams.first()
video.download()
print("Done.")
time.sleep(0.5)
os.system("cls")
for i in glob.glob("*.3gpp"):
    os.rename(i, "audio.3gpp")
print("Attempting to use ffmpeg to convert file to wav...")
try:
    subprocess.check_call(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(0.5)
    print("ffmpeg has been found! Continuing...")
    time.sleep(1)
except FileNotFoundError or subprocess.CalledProcessError:
    os.system("cls")
    print("ffmpeg is not installed. If you do have ffmpeg installed as a zip,")
    print(" make sure to extract it and that the 'bin' folder is on your C: drive and is on")
    print("PATH.")
    time.sleep(5)
    exit(0)
subprocess.run(['ffmpeg', '-y', '-i', 'audio.3gpp', '-ar', '48000', 'mono.wav'], stdout=subprocess.PIPE)
os.remove("audio.3gpp")
os.system("cls")
print("Done!")
time.sleep(2)
os.system("cls")
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