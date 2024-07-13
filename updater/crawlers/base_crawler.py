import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from abc import ABC, abstractmethod


class BaseAbstractCrawler(ABC):
    def __init__(self):
        self.headers = self.get_headers()
    
    @abstractmethod
    def get_headers(self):
        pass
    
    def send_request(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code
            return response
        except requests.exceptions.RequestException as e:
            raise SystemExit(f"Request failed: {e}")
    
    @abstractmethod
    def parse_response(self, response):
        pass
    
    def fetch_data(self, url):
        response = self.send_request(url)
        return self.parse_response(response)
