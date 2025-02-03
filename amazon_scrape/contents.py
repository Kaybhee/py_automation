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
    title = [span.text.strip() for span in title_spans]
    # price = ele_id.text.strip().replace("$", "").replace(",", "")
    return title[0]

def get_product_rating(soup):
    new_r = soup.find("span", attrs =  {"class" :"a-icon-alt"})
    ratings = [float(pr_rat.text.strip().split()[0]) for pr_rat in new_r]
    # new_r.find("span", class_ = "a-icon-alt" )
    return ratings

def product_info(links):
    products = {}
    print("The scraped link:", links)
        # print("This is obtaining the link:", i)
    html = get_html_parser(links)
    soup = BeautifulSoup(html, 'lxml')
    title = get_product_title(soup)
    price = get_product_prices(soup)
    rating = get_product_rating(soup)
    products["title"] = title
    products["Prices"] = price
    products["rating"] = rating
    print(products)
    # price = soup.find_all("div", {'class': "a-section a-spacing-none aok-align-center aok-relative"})
    # print(price)



if __name__== "__main__":
    with open('amazon_links.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            links = row[0]
            product_info(links)
