#!/usr/bin/env python

import requests
import urllib.request
from bs4 import BeautifulSoup


def main():
    url = 'https://www.surveymonkey.com/analyze/Rfx8SwzohZfx0v8pGJNUnSu4zeJBw2xDNXAneQeZZgc_3D'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("url", url)
    print("response", response)
    print("soup", soup)

    
if __name__ == "__main__":
    main()

