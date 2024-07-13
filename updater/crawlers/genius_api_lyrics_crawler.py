import os
from dotenv import load_dotenv
from base_crawler import BaseAbstractCrawler

class GeniusApiLyricsCrawler(BaseAbstractCrawler):
    def get_headers(self):
        return {
            "Authorization": f"Bearer {os.getenv('GENIUS_API_TOKEN')}"
        }
    
    def parse_response(self, response):
        info = response.json()
        hits = info["response"]["hits"]
        if hits:
            lyris_info = hits[0]
            return lyris_info["result"]["url"]
        return "No matching song found."
    
    def get_song_lyrics_url(self, artistname, trackname):
        query = f"{artistname} {trackname}"
        url = f"https://api.genius.com/search?q={query}"
        return self.fetch_data(url)

# 範例調用
if __name__ == "__main__":
    genius_crawler = GeniusApiLyricsCrawler()
    song_lyrics_url = genius_crawler.get_song_lyrics_url("Billie Eilish", "BIRDS OF A FEATHER")
    print(song_lyrics_url)
    
