from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random

class Navigator():
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        # options.set_headless(True)
        self.browser = webdriver.Chrome(executable_path="ChromeDriver\Windows\94.0.4606.41\chromedriver.exe", options=options)
        self.browser.set_window_size(930, 862)
        self.browser.
        self.url = "https://www.google.fr/"
    
    def start(self):
        self.browser.get(self.url)
        
if __name__ == "__main__":
    Navigator().start()