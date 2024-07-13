from dotenv import load_dotenv
from album_html_lyrics_crawler import AlbumHtmlLyricsCrawler
from  genius_api_lyrics_crawler import GeniusApiLyricsCrawler

if __name__ == "__main__":
    load_dotenv("../config/.env")
    genius_crawler = GeniusApiLyricsCrawler()
    album_crawler = AlbumHtmlLyricsCrawler()
    song_lyrics_url = genius_crawler.get_song_lyrics_url("Billie Eilish", "BIRDS OF A FEATHER")
    album_lyrics = album_crawler.get_album_lyrics(song_lyrics_url)
    print(album_lyrics)