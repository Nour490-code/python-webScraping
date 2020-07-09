import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://nour490-code.github.io/Easybank-landing-page/')

soup = BeautifulSoup(response.text,'html.parser')

boxes = soup.find_all(class_='box-2')

with open('articles.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title','Author']
    csv_writer.writerow(headers)
    for box in boxes:
        title = box.find(class_='title').get_text().replace('\n','')
        author = box.find(class_='authors').get_text().replace('\n','')
        csv_writer.writerow([title,author])
