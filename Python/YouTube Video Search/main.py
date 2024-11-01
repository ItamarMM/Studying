#This is only a small personal project that was started but never finished because It was not worth the effort since the library "youtubesearchpython" is not updated anymore nowadays, so It might not work in the future.


from youtubesearchpython import *

channelMaxAmountOfVideosDefault = 5
youtubeChannels = [["Eminem",5],["Shakira",2],["Michael Jackson",30]]

def downloadMp3(YoutubeVideoToDownload):
    print(YoutubeVideoToDownload)

def downloadMp3ByChannel(channelSearchInput, channelMaxAmountOfVideos = channelMaxAmountOfVideosDefault):
    channelsSearch = ChannelsSearch(channelSearchInput, limit = 10, region = 'US')
    channelResult = (channelsSearch.result()["result"][0])
    channelName = channelResult["subscribers"]
    print(channelName)
    channelId = channelResult["id"]
    print(channelId)
    playlist = Playlist(playlist_from_channel_id(channelId))
    print(f'Videos Retrieved: {len(playlist.videos)}')
    while playlist.hasMoreVideos:
        print('Getting more videos...')
        playlist.getNextVideos()
        print(f'Videos Retrieved: {len(playlist.videos)}')
    print('Found all the videos.')
    
    i = 0
    videoList = []
    while i < len(playlist.videos):
        link = playlist.videos[i]["link"]
        link = link.split("&list=")[0]
        views = (playlist.videos[i]["accessibility"]["title"]).split(" ")[-2].replace(",","")
        if views == "No":
            views = 0
            print(link)
        else:
            views = int(views)
        videoList.append([link,views])
        
        i += 1
    orderedVideoList = sorted(videoList, key=lambda x: int(x[1]), reverse=True)
    i = 0
    while i < channelMaxAmountOfVideos:
        i += 1
        downloadMp3(orderedVideoList[i])

def youtubeChannelsDownload():
    for channel in youtubeChannels:
        if channel[1]:
            downloadMp3ByChannel(channel[0],channel[1])
        else:
            downloadMp3ByChannel(channel[0],20)

def downloadMp3ByVideo(video):
    if video.startswith == "http://" or "https://" or "www.":
        downloadMp3(video)

def youtubeVideosDownload():
    videosSearch = VideosSearch("Gangnam Style", limit = 1)
    print(videosSearch.result())




def main():
    # youtubeChannelsDownload()
    youtubeVideosDownload()

    
if __name__ == "__main__":
    main()