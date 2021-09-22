import lxml.html
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.scraping
collection = db.books
collection.delete_many({})