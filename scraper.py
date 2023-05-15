from bs4 import BeautifulSoup
import requests
import re
import math


def get_element_value(review, tag, attribute):
    e = review.find(tag, class_=attribute)
    return None if e is None or e.text is None else e.text.replace("\n", " ")


def get_element_size(review, tag, attribute):
    e = review.find_all(tag, class_=attribute)
    return len(e.text) if e is not None else 0


def get_review_data(review):
    e = review.find_all("time")
    return None if len(e) == 0 else e[0].get('datetime')


def get_purchase_date(review):
    e = review.find_all("time")
    return None if len(e) < 2 else e[1].get('datetime')


class Scraper:

    def __init__(self, product_id):
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

        opinion_number = int(re.search(r'\d+', elements[2].text if
                             re.search(r'\d+', elements[2].text) else "0").group())
        if opinion_number > 500:
            raise Exception("This Product has too many opinions, enter a different product id")

        reviews = []
        page, all_pages = 1, math.ceil(opinion_number / 10)

        while page <= all_pages:
            soup = BeautifulSoup(requests.get(f'https://www.ceneo.pl/{self.product_id}'
                                              f'/opinie-{str(page)}').text, 'html.parser')
            reviews.extend(self.remove_empty(soup.find_all("div", class_="user-post__body")))
            page += 1

        return reviews

    def remove_empty(self, user_reviews):
        return [self.get_details(i) for i in user_reviews if
                self.get_details(i)["author"] is not None and self.get_details(i)["score"] is not None]

    @staticmethod
    def get_details(review):
        ft = review.find_all("div", class_="review-feature__col")
        details = {"author": get_element_value(review, "span", "user-post__author-name"),
                   "comment_date": get_review_data(review),
                   "purchase_date": (get_purchase_date(review) or "0"),
                   "opinion": get_element_value(review, "div", "user-post__text"),
                   "recommendation": (get_element_value(review, "em", "recommended") or "Nie polecam"),
                   "score": get_element_value(review, "span", "user-post__score-count"),
                   "likes": review.find("button", class_="js_vote-yes").find("span").text if review.find(
                       "button", class_="js_vote-yes") else '0',
                   "dislikes": review.find("button", class_="js_vote-no").find("span").text if review.find(
                       "button", class_="js_vote-no") else '0',
                   'pros': [p.text for p in ft[0].findChildren("div", recursive=False)
                            if 'review-feature__item' in p['class']] if len(ft) > 0 else '0',
                   'cons': [c.text for c in ft[1].findChildren("div", recursive=False)
                            if 'review-feature__item' in c['class']] if len(ft) > 1 else '0'
                   }

        return details
