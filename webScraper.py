from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.youtube.com/feed/trending').text

soup = BeautifulSoup(source ,"lxml")

csv_file = open('youtube_scrappper.csv' , 'w'  ,encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Video Title' , 'Views' , 'Video Link'])

for content in soup.find_all('div' ,class_="yt-lockup-content"):

    try:
        Vid_title = content.a.text
        print(Vid_title)


        views = content.find_all('li')[1].text
        print(views)

        token  = content.a['href']
        link = f'https://www.youtube.com{token}'
        print(link)

        print()

    except Exception as e:
        print(None)

    csv_writer.writerow([Vid_title, views, link])

csv_file.close()


