from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def StartSearch():

    search = input("Search for:")
    params = {"q": "search"}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)


    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findALL("a", {"class": "thumb"})

    for item in links:
        try:
            image_obj = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            #[-1] to get the last item

            try:
                img = Image.open(BytesIO(image_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Could not save image")
        except:
            print("Could not request image")

        StartSearch()

StartSearch()
