from bs4 import BeautifulSoup
from base_crawler import BaseAbstractCrawler

class AlbumHtmlLyricsCrawler(BaseAbstractCrawler):
    def get_headers(self):
        return {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
    
    def parse_response(self, response):
        html = BeautifulSoup(response.text, 'html.parser')
        span_elements = html.find_all('span', class_='ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw')
        br_elements = html.find_all('div', {'data-lyrics-container': 'true'})
        
        lyrics_list = []
        for lyrics in br_elements:
            lyrics_list.append(lyrics.get_text())
        for lyrics in span_elements:
            lyrics_list.append(lyrics.get_text())
        
        if not lyrics_list:
            return "No lyrics found."
        
        return '\n'.join(lyrics_list)
    
    def get_album_lyrics(self, source_url):
        return self.fetch_data(source_url)

# 範例調用
if __name__ == "__main__":
    album_crawler = AlbumHtmlLyricsCrawler()
    album_lyrics = album_crawler.get_album_lyrics("https://genius.com/Kendrick-lamar-not-like-us-lyrics")
    print(album_lyrics)
