from bs4 import BeautifulSoup
import requests
import re
import math


class Scraper:

    def __int__(self, product_id):
        self.product_id = product_id
        self.product_url = requests.get(self.get_url())
        self.soup = BeautifulSoup(self.product_url.text, 'html.parser')


    def get_product_name(self):
        return get_element_value(self.soup, "h1", "product-top__product-info__name") or "No-name"

    def get_url(self):
        return f'https://www.ceneo.pl/{self.product_id}#tab=reviews'

    def get_all_opinions(self):
        elements = self.soup.find_all('span', class_='page-tab__title js_prevent-middle-button-click')
        if not elements:
            raise Exception("Product with this ID does not exist!")

        opinion_number = int(re.search(r'\d+', elements[2] if elements[2] else "0"))
        reviews = []
        pages_number = math.ceil(opinion_number / 10)

        if opinion_number > 500:
            raise Exception("This Product has too many opinions, enter a different product id")

def get_element_value(review, tag, attribute):
    e = review.find(tag, class_=attribute)
    return None if e is None or e.text is None else e.text.replace("\n", " ")

def get_element_size(review, tag, attribute):
    e = review.find_all(tag, class_=attribute)
    return len(e.text) if e is not None else 0

def get_review_data(review):
    e = review.find_all("time")
    return None if len(e) == 0 else e[0].get('datetime')

def get_purhase_date(review):
    e = review.find_all("time")
    return None if len(e) < 2 else e[1].get('datetime')
