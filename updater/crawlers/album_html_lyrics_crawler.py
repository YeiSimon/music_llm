from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from base_crawler import BaseAbstractCrawler

class AlbumHtmlLyricsCrawler(BaseAbstractCrawler):
    def get_headers(self):
        ua = UserAgent()
        user_agent = ua.random
        return {'user-agent': user_agent}
        
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
    album_lyrics = album_crawler.get_album_lyrics("https://genius.com/Travis-scott-fe-n-lyrics")
    print(album_lyrics)
