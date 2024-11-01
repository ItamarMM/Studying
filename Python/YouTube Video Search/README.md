# YouTube Mp3 Downloader
The idea behind this, was to use youtubesearchpython Python library as a base for the project. So I would be able to extract mp3 files in a convenient way, so I started by filtering the "x" most viewed videos links from a channel search and then I would add a function/use an already created one to actually download the files.

## What did I learn here?
- Sorting dictionaries/lists.
- Tried to organize myself better with functions from the start.
- To use a, [now discontinued, YouTube search Python library (youtubesearchpython), but that will probably keep working for years](https://github.com/alexmercerind/youtube-search-python/issues/189). This demotivated me to continue creating the script, despite the fact that the library is currently functional.

## What is working?
- Searching top 1 YouTube channel by name of the channel.
- Search top x amount of most viewed videos by the YouTube found channel.

## How to use the script
"youtubeChannels" variable is a list, whose first parameter must be the channel to be searched, and whose second parameter of the list must be an integer that is the max number of videos to download.

## What could be added?
- More types of inputs apart from "youtubeChannels", like: youtubePlaylist and youtubeVideos.
- Allow to use links instead of Name to search (Right now if you use a link instead of a channel name, It just would not work)
- Improve the way of inputting the data:
    - Importing csvs as inputs. > So you could use a "Type" (YouTube Channel,Playlist,Video)
    - Create a GUI (using f.e. [DearPyGUI](https://pypi.org/project/dearpygui/))
- Modify the "Downloading function" to actually download the video as a .mp3 file instead of showing the url of the video.
