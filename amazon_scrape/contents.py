from  bs4 import BeautifulSoup
import csv
import requests
from datetime import datetime
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

def product_list(soup):
    details = {}
    pr_table = soup.find("div", id = "prodDetails")
    pr_table_data = pr_table.findAll("table", class_ = "productDetails_detailBullets_sections1")
    for table in pr_table_data:
        table_rows = table.findAll("tr")
        for row in table_rows:
            row_key = row.find("th").text.strip() 
            row_value = row.find("td").text.strip()
            # print(row_key)
            details[row_key] = row_value
    return details

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
    # table = product_list(soup)

    products["title"] = title
    products["Prices"] = price
    products["rating"] = rating
    # products["Products"] = table
    # add_details = 
    products.update(product_list(soup))
    # return add_details
    return products



if __name__== "__main__":
    product_table = []
    with open('amazon_links.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            links = row[0]
            product_table.append(product_info(links))
            # product_table.append(
    #         print(product_table)
    file_name = "Output file - {}.csv".format(datetime.today().strftime("%m-%d-%Y"))
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(product_table[1].keys())
        for product in product_table:
            writer.writerow(product.values())

