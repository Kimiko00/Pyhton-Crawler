from dotenv import load_dotenv
from flask import Flask

import requests, os

class NvdAPI:
    def config():
        load_dotenv()
    
    def __init__(self):
        self.url = os.getenv('url')
        
    def fetch_cves(self):
        url = f"{self.url}/cves/2.0"
        response = requests.get(url)
        return response.json()
        
    