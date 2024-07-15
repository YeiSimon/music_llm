import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class BaseAbstractCrawler(ABC):
    def __init__(self, proxies=None):
        self.headers = self.get_headers()
        self.proxies = proxies
    
    @abstractmethod
    def get_headers(self):
        pass
    
    def send_request(self, url):
        try:
            response = requests.get(url, headers=self.headers, proxies=self.proxies)
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
