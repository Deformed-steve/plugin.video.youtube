import requests

class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_popular_videos(self):
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&key={self.api_key}"
        response = requests.get(url).json()
        return [{
            "title": item["snippet"]["title"],
            "url": f"plugin://plugin.video.youtube/play/?video_id={item['id']}"
        } for item in response.get("items", [])]
