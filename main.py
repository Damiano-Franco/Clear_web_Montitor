import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup

while True:
	try:
		response = requests.get(
		url='https://proxy.scrapeops.io/v1/',
		stream=True,
		params={
		'api_key': 'xxxxxxxxxxxx',
		'url': 'https://nome_sito.org',
		},
		)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
			print("An error occurred:", e)
    
	if response:
		print(response)
		soup = BeautifulSoup(response.content, 'html.parser')
		classified = soup.find_all('div', class_= "stabview-row")

		for row in classified:
			title_raw = row.find('div', class_="stabview-row-subject").find_all("a")
			#for a in link:
			title = title_raw[1].text

			user_raw = row.find('span', class_="stabview-row-lastavatars-username").find("a")
			#for a in link:
			user = user_raw.text

			date_raw = row.find('div', class_="stabview-row-item stabview-row-dateline")
			#for a in link:
			date = date_raw.text

			category_raw = row.find('div', class_="stabview-row-item stabview-row-category").find("a")
			#for a in link:
			category = category_raw.text

			print(title,user,date,category)

			#print(title,user,date,category)
			classified = f"{title},{user},{date},{category}\n"

			read_csv = open('nome_sito.csv', 'r')
			Lines = read_csv.readlines()
			eof = len(Lines)
			print(eof)
	
			count = 0
			
			for line in Lines:
				count += 1

				if classified == line:
					print("uguale")
					break
				elif eof == count:
					read_csv.close
					f = open("nome_sito.csv", "a")
					f.write(classified)
					f.close()
					break
				else:
					pass

			read_csv.close

		time.sleep(3600)