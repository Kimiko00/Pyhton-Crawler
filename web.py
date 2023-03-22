import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = "https://nasional.tempo.co/"
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the article titles, authors, and dates
titles = soup.findAll("h2", class_="title")
authors = soup.findAll("div", class_="author")
dates = soup.findAll("h4", class_="date")
images = soup.findAll('img')



# print the information of e
# print the information of each article
for i in range(len(titles)):
    print("Title:", titles[i].text.strip())
    # print("Author:", authors[i].text.strip())
    print("Date:", dates[i].text.strip())
    print("URL:", titles[i].find("a")["href"])
    print("Image:", images[i]['src'])
    print("")

#sed this sid kontol
#this is a new line