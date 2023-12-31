from pytube import YouTube
from pathlib import Path
import sys
import os

current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
config_file_path = os.path.join(current_directory, 'links.txt')

def remove_char(filename):
    unwanted_chars = "<>/|*\"?'."
    translation_table = str.maketrans("", "", unwanted_chars)
    new_text = filename.translate(translation_table)
    return new_text


with open(config_file_path, 'r') as file:
    links = []
    destination = ""

    for line in file:
        stripped_line = line.strip()
        if stripped_line.startswith('#'):
            continue
        elif stripped_line.startswith('!'):
            destination = stripped_line[1:]
        else:
            links.append(stripped_line)

num = 0
for i in links:
    num += 1
    progres = round(100 / (len(links) / num))

    yt = YouTube(i)
    file_name = remove_char(yt.title) + '.mp3'
    full_file_path = os.path.join(destination, file_name)

    if not Path(full_file_path).is_file():
        video = yt.streams.filter(only_audio = True).first()
        out_file = video.download(output_path = destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(f'{progres}% | Downloaded 🟢 | {yt.title}')
    else:
        print(f'{progres}% | File already exist 🔴 | {yt.title}')

input("Press enter to exit...")
