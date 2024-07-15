import os
from fuzzywuzzy import fuzz
from dotenv import load_dotenv
from base_crawler import BaseAbstractCrawler
from errors import ScrabbleException

class GeniusApiLyricsCrawler(BaseAbstractCrawler):
    def __init__(self):
        self.query = None
        super().__init__()
        
    def get_headers(self):
        return {
            'Authorization' : f"Bearer {os.getenv('GENIUS_API_TOKEN')}"
        }
    
    def parse_response(self, response):
        info = response.json()
        hits = info["response"]["hits"]
        high_score, high_score_url = 0, None
        if hits:
            for hit in hits[:3]:
                full_title = hit["result"]["full_title"]
                fuzz_score = fuzz.token_sort_ratio(self.query, full_title)
                if fuzz_score > high_score:
                    high_score = fuzz_score
                    high_score_url = hit["result"]["url"]
                    
            return high_score_url

        raise 
    
    def get_song_lyrics_url(self, artistname, trackname):
        self.query = f"{artistname} {trackname}"
        try:
            url = f"https://api.genius.com/search?q={self.query}"
        except Exception:
            raise
        return self.fetch_data(url)

# 範例調用
if __name__ == "__main__":
    load_dotenv("../config/.env")
    genius_crawler = GeniusApiLyricsCrawler()
    song_lyrics_url = genius_crawler.get_song_lyrics_url("Alibi", "Sevdaliza, Pabllo Vittar, Yseult")
    print(song_lyrics_url)
    
