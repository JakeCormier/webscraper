from bs4 import BeautifulSoup
import requests


search = input("Enter Search Term: ")
params = {"q": search}
r = requests.get("http://bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    #attr attributes

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Parent:", item.find("a").parent)


        children = item.find("h2")
        print("Next sibling of the h2:", children.next_sibling)

        '''children = item.children
        for child in children:
            print("Child:", child)'''
