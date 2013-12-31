"""
This script fetches the titles and urls to the top 100 most popular ebooks (by download)
on gutenberg.org. It returns a dictionary called 'books' with key=title and value=url.
"""
import urllib2
from bs4 import BeautifulSoup

def fetch_gutenberg_top_100():
    base_url = "http://www.gutenberg.org"
    guten_1_25 = "http://www.gutenberg.org/ebooks/search/?sort_order=downloads"
    guten_26_50 = "http://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index=26"
    guten_51_75 = "http://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index=51"
    guten_76_100 = "http://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index=76"
    guten_urls = []
    guten_urls.extend([guten_1_25, guten_26_50, guten_51_75, guten_76_100])
    books = {}
    for url in guten_urls:
        response = urllib2.urlopen(url)
        html = response.read()

        soup = BeautifulSoup(html)
        for book in soup.find_all('li', class_='booklink'):
            subtitle = book.find('span', class_='subtitle')
            title=book.find('span', class_='title').text
            link = book.find('a', class_='link').get('href')
            books[title]=base_url + str(link) + '.txt.utf-8'
    return books
