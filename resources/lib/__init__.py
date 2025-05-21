import xbmcgui, xbmcplugin, sys
from youtube_api import YouTubeAPI

def main():
    api = YouTubeAPI("AIzaSyCKhnfWDTcn3jQIY7mqr06gChhJj313P5s")  # Replace with your key!
    videos = api.get_popular_videos()
    for video in videos:
        li = xbmcgui.ListItem(video["title"])
        xbmcplugin.addDirectoryItem(int(sys.argv[1]), video["url"], li)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == "__main__":
    main()
