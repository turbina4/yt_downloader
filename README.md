# YouTube Downloader

## Description

This program allows you to easily download Youtube videos in MP3 or MP4 by providing a list of video links in a configuration file (`links.txt`). The script uses the `pytube` library to handle YouTube video processing and the `pathlib` library for file path manipulation.

## Usage

1. Edit a file named `links.txt` in the same directory as the script.
2. Add YouTube video links to the `links.txt` file, one per line.
3. Specify the destination folder for downloaded MP3 files by adding a line starting with `!` followed by the folder path.
4. Run the program.

## Example `links.txt`

```txt
# CONFIG FILE
# After the exclamation mark (!), provide the path to the folder where the mp3 files will be downloaded
# Everything after the hashtag (#) is ignored
# Add links one below the other
# Empty lines are not allowed
!C:/Users/Username/Music/YoutubeDownloads
https://www.youtube.com/watch?v=example_video_id_1
https://www.youtube.com/watch?v=example_video_id_2
```

## Notes

-   Lines starting with # are treated as comments and ignored.
-   Empty lines in the configuration file are not allowed.
-   The script automatically removes unwanted characters from the video title to create a clean file name. Note that titles may slightly differ due to removed characters.

## Icon

The application icon can be downloaded [here](https://www.flaticon.com/free-icon/mp3_9798029?term=mp3+file&page=1&position=8&origin=tag&related_id=9798029)

---

**Remember to leave a star! 💪**