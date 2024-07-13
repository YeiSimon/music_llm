import os
import spotipy
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from base_crawler import BaseAbstractCrawler
from spotipy.oauth2 import SpotifyClientCredentials

@dataclass
class TrackFeatures:
    danceability: float
    energy: float
    key: int
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    
class SpotifyApiCrawler(BaseAbstractCrawler):
    def __init__(self):
        self.sp = self._authenticate_spotify()
        super().__init__()
        
    def _authenticate_spotify(self):
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    def get_headers(self):
        # Spotipy handles headers internally, so we return an empty dictionary here
        return {}
    
    def send_request(self, url):
        # Override send_request to use Spotipy instead of requests
        pass
    
    def parse_response(self, response):
        pass
    
    def fetch_data(self, uris):
        features_list = []

        for uri in uris:
            features = self.sp.audio_features(tracks=[uri])
            for feature in features:
                if feature:
                    track_features = TrackFeatures(
                        danceability=feature['danceability'],
                        energy=feature['energy'],
                        key=feature['key'],
                        loudness=feature['loudness'],
                        speechiness=feature['speechiness'],
                        acousticness=feature['acousticness'],
                        instrumentalness=feature['instrumentalness'],
                        liveness=feature['liveness'],
                        valence=feature['valence'],
                        tempo=feature['tempo']
                    )
                    features_list.append(track_features)

        return features_list

if __name__ == "__main__":
    load_dotenv(Path("../config/.env"))
    
    # 創建 Spotify 爬蟲實例
    spotify_crawler = SpotifyApiCrawler()
    
    # 需要獲取音軌信息的 URI 列表
    track_uris = ["spotify:track:4uLU6hMCjMI75M1A2tKUQC", "spotify:track:1301WleyT98MSxVHPZCA6M"]
    
    # 獲取音軌信息並打印
    track_info_list = spotify_crawler.fetch_data(track_uris)
    
    # 將數據轉換為 DataFrame 並打印
    track_info_df = pd.DataFrame([t.__dict__ for t in track_info_list])
    print(track_info_df)