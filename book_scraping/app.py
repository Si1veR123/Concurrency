"""
This is the main file for the program
It receives the html file and prints data
Order of files in this project app.py > page.py > BookParser.py > locators.py
"""


import asyncio, aiohttp, time
from Asychronous_Development.book_scraping.Page_Scraper.page import Page

async def get_html(page, session):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    async with session.get(url) as response: # get url html
        return await response.read() # reads the response, you must await it as .read() is a co-routine


async def main_coro():
    async with aiohttp.ClientSession(loop=loop) as session: # make a aiohttp session
        tasks = [get_html(page, session) for page in range(1, 51)] # makes a list of co-routines with each page passed as an arg
        gathered_tasks = asyncio.gather(*tasks) # awaits each task and only returns when all complete
        return await gathered_tasks # awaits the gathered_tasks results and returns it

start = time.time() # used to time the script

all_pages = [] # stores Page objects for each page
all_pages_content = [] # keeps a list for every page. Each list that contains Parser objects, that contain data on the title, rating and author
loop = asyncio.get_event_loop() # get event loop to run co-routines in
html = loop.run_until_complete(main_coro()) # runs the main co-routine in event loop until it returns and finishes
for page in html:
    # Page makes the BeautifulSoup
    all_pages.append(Page(page))

for page in all_pages:
    all_pages_content.append(page.books())

# converts rating from string to integer
rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}


book_count = 0
# print all of the books' data
for page in all_pages_content: # iterates through each list in all_pages_content
    for book in page: # each list has an object for each book that has its properties
        print(f'Book: {book.get_book()}')
        print(f'Rating: {rating_dict[book.get_rating()]}')
        print(f'Price: £{book.get_price()}\n')
        book_count += 1
print(f'Number of books: {book_count}')
print(f'Time took: {(time.time() - start)}')