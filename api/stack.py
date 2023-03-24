from dotenv import load_dotenv
from flask import Flask

import requests, os

class StackOverflowAPI:
    def config():
        load_dotenv()
        
    def __init__(self):
        self.base_url = os.getenv('base_url')
        self.headers = {"Accept-Encoding": "gzip"}
        
    def fetch_questions(self, order="desc", sort="activity", site="stackoverflow"):
        url = f"{self.base_url}/questions"
        params = {"order": order, "sort": sort, "site": site}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
