from loguru import logger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from timeit import default_timer as timer

import os
import random


def search(mode):
    if mode == 'desktop':
        x = 0
        while x < 30:
            word = random.choice(WORDS)
            search_form = driver.find_element_by_class_name('b_searchbox')
            search_form.clear()
            search_form.send_keys(word)
            search_form.submit()
            x += 1
            logger.debug(f'Desktop searched {word} {x}/30')
    elif mode == 'mobile':
        x = 0
        while x < 20:
            word = random.choice(WORDS)
            search_form = driver.find_element_by_id('sb_form_q')
            search_form.clear()
            search_form.send_keys(word)
            search_form.submit()
            x += 1
            logger.debug(f'Mobile searched {word} {x}/20')


path = os.getcwd() + '\\chromedriver.exe'
profile_path = 'C:\\Users\\arlan\\AppData\\Local\\Google\\Chrome\\User Data'

word_file = os.getcwd() + '\\words.txt'
WORDS = open(word_file).read().splitlines()

desktop_options = Options()
desktop_options.add_argument('user-data-dir=' + profile_path)
# disables chrome logging on terminal
desktop_options.add_experimental_option('excludeSwitches', ['enable-logging'])
desktop_options.headless = True

mobile_options = Options()
mobile_options.add_argument('user-data-dir=' + profile_path)
mobile_options.add_experimental_option('excludeSwitches', ['enable-logging'])
mobile_emulation = {"deviceName": "Pixel 2"}
mobile_options.add_experimental_option("mobileEmulation", mobile_emulation)
mobile_options.headless = True

t_start = timer()
with Chrome(executable_path=path, options=desktop_options) as driver:
    driver.implicitly_wait(3)
    driver.get('https://bing.com')
    logger.debug('Accessing desktop browser')
    search('desktop')
    logger.debug('Quitting desktop browser')

with Chrome(executable_path=path, options=mobile_options) as driver:
    driver.implicitly_wait(3)
    driver.get('https://bing.com')
    logger.debug('Accessing mobile browser')
    search('mobile')
    logger.debug('Quitting mobile browser')

t_end = timer()
logger.debug('Ran script in ' + str(t_end - t_start) + 's')
