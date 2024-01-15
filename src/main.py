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


extension = input(str("Download in mp4? (y=mp4,n=mp3) [y/n]: "))

for num, i in enumerate(links, 1):
    progres = round(100 / len(links) * num)

    yt = YouTube(i)
    full_file_path = os.path.join(destination, remove_char(yt.title) + '.mp3')

    if not Path(full_file_path).is_file():
        out_file = None

        if extension == "y":
            out_file = yt.streams.filter(progressive = True, file_extension = 'mp4').order_by(
                'resolution').desc().first().download(output_path = destination)
        elif extension == "n":
            out_file = yt.streams.filter(only_audio=True).first().download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

        print(f'{progres}% | Downloaded 🟢 | {yt.title}')
    else:
        print(f'{progres}% | File already exist 🔴 | {yt.title}')

input("Press enter to exit...")
