thonimport requests
from bs4 import BeautifulSoup
import time

class ContentExtractor:
    def __init__(self, url, selector):
        self.url = url
        self.selector = selector
        self.previous_content = None

    def get_content(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.select_one(self.selector).text.strip()

    def get_previous_content(self):
        return self.previous_content

    def take_screenshot(self):
        # Placeholder for screenshot taking logic
        return f"https://example.com/screenshots/{int(time.time())}.png"

    def save_content(self, content):
        self.previous_content = content