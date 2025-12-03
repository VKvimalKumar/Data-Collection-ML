from bs4 import BeautifulSoup
import csv

html = open("index.html").read()
soup = BeautifulSoup(html, "html.parser")

acts = [a.text for a in soup.select(".act")]

with open("activity_scraped.csv", "w", newline="") as wcsv:
    writer = csv.writer(wcsv)
    writer.writerow(["activity"])
    for act in acts:
        writer.writerow([act])

print("Scraped:", len(acts))
