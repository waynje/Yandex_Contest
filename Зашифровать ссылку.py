import random
import string


class MarsURLEncoder:

    def __init__(self):
        self.url_collection = {}

    def generate_key(self):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return key

    def encode(self, long_url):
        key = self.generate_key()
        self.url_collection[key]=long_url
        short_url = 'https://ma.rs/' + key
        return short_url

    def decode(self, short_url):
        key = short_url.split('/')[-1]
        if key in self.url_collection:
            long_url = self.url_collection[key]
        else: 
            return 'Invalid URL!'
        return long_url