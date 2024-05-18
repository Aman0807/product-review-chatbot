from bs4 import BeautifulSoup
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

url = "https://www.amazon.in/LG-Convertible-Anti-Virus-Protection-TS-Q19YNZE1/dp/B0CSG14M2C/ref=sr_1_3?crid=31W28NDSXHNIV&dib=eyJ2IjoiMSJ9.EojAJc_6Dkt90gdXHaSDyCc3xjf-yr4516NEDEo560OkjiSyvu8AeTa75lqVGbX0eSPC4898JExFGJnnOSqBBJ-GuZcxkYDb9RUDt8n4QKl8JGxwbi0RfX1DvBoFlhv4OEa6r7lYODWcRdYa2k2x8Xf1J8eC40xyvqgofZp7YTuv2hZYNfceNLsW8Y7Y0_w3iMK1wUTRsLWN54FeqpeuCiFCI6M99MyoRi5m2dX-qfQ.gSN5717voahpps3xvVep_-TJ05Fu4ByPYmOfdb3MHrA&dib_tag=se&keywords=air%2Bconditioner&qid=1711960333&sprefix=air%2Bcon%2Caps%2C233&sr=8-3&th=1"


r = requests.get(url=url, headers=headers)
# print(r.content)

content = r.content
soup = BeautifulSoup(content)

all_reviews = []

# for d in soup.findAll():
reviews = soup.findAll('div', {'data-hook': 'review'})
reviews = reviews[:min(20, len(reviews))]

for i in reviews:
    rev_title = i.find('a', {'data-hook': 'review-title'}).text.strip()
    rev_rating = i.find('i', {'data-hook': 'review-star-rating'}).text.strip()
    rev_text = i.find('div', {'data-hook': 'review-collapsed'}).text.strip()
    

    review = {
        "rev_title": rev_title,
        "rev_rating":rev_rating,
        "rev_text":rev_text
    }

    all_reviews.append(review)

    with open("amazon_reviews.json", 'a') as f:
        json.dump(review, f)


print(all_reviews)




