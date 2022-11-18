from urllib import response
import requests

def main():
    url = "https://google.com"
    response = requests.get(url)
    print(response)
    