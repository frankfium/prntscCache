import random
import string
import os
import webbrowser
from random import randint
import image_scraper
import urllib
from bs4 import BeautifulSoup

def func():
    lower_upper_alphabet = string.ascii_lowercase
    url = 'http://prnt.sc/'
    path = "Pictures/cache"
    urls = []
    for i in range(10):
        num1 = str(randint(0,9))
        num2 = str(randint(0,9))
        num3 = str(randint(0,9))
        num4 = str(randint(0,9))
        let1 = random.choice(lower_upper_alphabet)
        let2 = random.choice(lower_upper_alphabet)
        urlfin = url + let1 + let2 + num1 + num2 + num3 + num4
        print(urlfin)
        req = urllib.request.Request(urlfin)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0")
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html)
        imgs = soup.find("img", {"class":"no-click screenshot-image"})
        finished = imgs["src"]
        urls.append(finished)
    print(urls)

    for url in urls:
        if "st" in url:
            print("")
        else:
            webbrowser.open_new_tab(url)

def main():
    func()

if __name__ == "__main__":
    main()
