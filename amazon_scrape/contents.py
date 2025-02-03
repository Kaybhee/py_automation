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
    price = soup.find("span", class_ = "a-price-whole")
    pr = [pr.text.strip().replace(".", "") for pr in price]
    return pr[0]



def get_product_title(soup):
    title_spans = soup.find("span", id = "productTitle")
    for span in title_spans:
        title = span.text.strip()
    # price = ele_id.text.strip().replace("$", "").replace(",", "")
        return title 

def product_info(links):
    products = {}
    print("The scraped link:", links)
        # print("This is obtaining the link:", i)
    html = get_html_parser(links)
    soup = BeautifulSoup(html, 'lxml')
    title = get_product_title(soup)
    price = get_product_prices(soup)
    products["title"] = title
    products["Prices"] = price
    print(products)
    # price = soup.find_all("div", {'class': "a-section a-spacing-none aok-align-center aok-relative"})
    # print(price)



if __name__== "__main__":
    with open('amazon_links.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            links = row[0]
            product_info(links)
