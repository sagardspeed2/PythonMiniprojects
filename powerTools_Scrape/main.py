from bs4 import BeautifulSoup
import requests as req
import csv
import os.path

url_fileName = "url_list.csv"

with open(url_fileName, 'r') as rf:

    reader = csv.reader(rf, delimiter=',')
    
    for row in reader:
        url = row[2]
        url = url[:-1]
        url = url[2:]
        url = url[:-1]

        webText = req.get(url)

        print(url)

        soup = BeautifulSoup(webText.text, "html.parser")

        fileName = "engine.csv"

        with open(fileName, 'a', newline='') as file:

            fileEmpty = os.stat(fileName).st_size == 0

            writer = csv.writer(file)

            if fileEmpty:
                writer.writerow(["SN", "Make", "Engine", "Product Name", "Product Link"])

            # GET MAKE NAME
            make_name = soup.find("span", {"class": "am-filter-value"})
            make_name = make_name.get_text()

            selWrapeer = soup.find("li", {"data-container": "engine"})

            # ENGINE NAME
            engine_name = selWrapeer.findChildren("span", {"class": "am-filter-value"})
            for child in engine_name:
                engine_name = child.get_text()

            productsArray = soup.find("ol", {"class": "product-items"})

            count = 1

            for prod in productsArray.findAll('li'):

                # PRODUCT NAME
                productName = prod.findAll("div", {"class": "product_title"})
                for child in productName:
                    productName = child.get_text()

                # PRODUCT LINK
                productLink = prod.find("a")
                productLink = productLink.get('href')

                writer.writerow([count, make_name, engine_name, productName, productLink])
                count += 1
    