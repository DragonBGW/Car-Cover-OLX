import requests
from bs4 import BeautifulSoup
import csv

# OLX Search URL
url = "https://www.olx.in/items/q-car-cover"

# Headers to avoid bot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Open output TSV file
with open("olx_car_covers.tsv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerow(["Title", "Price", "Location", "URL"])

    # Parse listings
    for item in soup.select("li[data-aut-id='itemBox']"):
        title = item.select_one("span._2tW1I").text if item.select_one("span._2tW1I") else "N/A"
        price = item.select_one("span._89yzn").text if item.select_one("span._89yzn") else "N/A"
        location = item.select_one("span._2FyGJ").text if item.select_one("span._2FyGJ") else "N/A"
        link_tag = item.select_one("a")

        link = "https://www.olx.in" + link_tag['href'] if link_tag and 'href' in link_tag.attrs else "N/A"
        writer.writerow([title, price, location, link])

print("Search results saved to olx_car_covers.tsv")
