"""
Extracts data from each book
"""

from Asychronous_Development.book_scraping.Locators.locators import Locators
import re

# custom error
class CostNotFound(ValueError):
    pass

class Parser:
    def __init__(self, parent):
        # parent is all of the book's location
        self.parent = parent

    def get_book(self):
        locator = Locators.title
        # gets the next book's title
        return self.parent.select_one(locator).attrs['title']

    def get_rating(self):
        locator = Locators.rating
        # gets the next book's rating
        rating_tag =  self.parent.select_one(locator).attrs['class']
        return [tag for tag in rating_tag if tag != 'star-rating'][0]

    def get_price(self):
        locator = Locators.price
        # get cost
        cost_tag = self.parent.select_one(locator).string
        # regex expression
        search = "£(\d+\.\d+)"
        price_match = re.search(search, cost_tag)
        # returns cost if price is found
        if price_match:
            # gets group 1 (brackets of regex expression) and returns as float
            return float(price_match.group(1))
        # else, raises error
        else:
            raise CostNotFound('Price was not found when scraping')