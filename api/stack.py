from flask import Flask
import requests

class StackOverflowAPI:
    
    def __init__(self):
        self.base_url = "https://api.stackexchange.com/2.3"
        self.headers = {"Accept-Encoding": "gzip"}
        
    def fetch_questions(self, order="desc", sort="activity", site="stackoverflow"):
        url = f"{self.base_url}/questions"
        params = {"order": order, "sort": sort, "site": site}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
