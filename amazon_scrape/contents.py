from  bs4 import BeautifulSoup
import csv
import requests
from selenium import webdriver
soup = BeautifulSoup()

def get_html_parser(links):
    res = requests.get(url=links)
    return res.content
    # soup = BeautifulSoup(res.text)
    # return res.content

def get_product_prices(soup):
    price_container = soup.find("div", {"class" : "a-section a-spacing-none aok-align-center aok-relative"})
    prices = price_container.find("span", {"class" : "aok-offscreen"})
    for price in prices:
         = price.text.strip().replace("$", "").replace(",", "")



    pass


def get_product_title(soup):
    # ele_id = soup.findAll('div', {"a-section a-spacing-none aok-align-center aok-relative"})
    price_spans = soup.find("div", id = "titleSection")
    for span in price_spans:
        price = span.text.strip()
    # price = ele_id.text.strip().replace("$", "").replace(",", "")
        print(price)

def product_info(links):
    products = {}
    print("The scraped link:", links)
        # print("This is obtaining the link:", i)
    html = get_html_parser(links)
    soup = BeautifulSoup(html, 'lxml')

    products["Title"] = get_product_title(soup)
    print(products)
    # price = soup.find_all("div", {'class': "a-section a-spacing-none aok-align-center aok-relative"})
    # print(price)



if __name__== "__main__":
    with open('amazon_links.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            links = row[0]
            print(product_info(links))
