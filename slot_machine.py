#
# slot_machine.py
# Created by Hexapetalous on Jan 5, 2016.
#
# This is a part of C0001, a short url getter of github.com.
#
# Copyright (c) 2016 Hexapetalous. All rights reserved.
# This code is licensed under MIT License.
#
"""
The basic logic here is to try every simple string of original name into the
shorten system and find which is both short enough and unused.
Now I finish it. And a thought came to me: why not try to visit a shortened url
and find out both what its original name is and whether it has been used? I
think I'm stupid. It must be caused of that the time is too late(3:31).
Fix it when I open this code next time. *_*
"""
import requests
import logging


MAX_LENGTH = 6  # Max trying url's length.
MAX_URL_LENGTH = 2  # Max result url's length.
POST_URL = 'http://git.io/create'
POST_URL_PREFIX = 'https://github.com/'
GET_URL_PREFIX = 'https://github.com/'
# For easy to code I make charset unchangeable.

global_str = None


def change_global_str():
    global global_str
    if global_str is None:
        global_str = min_str()
        return
    if global_str == max_str():
        global_str = None
        return
    for i in range(MAX_LENGTH):
        new, inc = increase(global_str[i])
        global_str = global_str[:i] + new + global_str[i + 1:]
        if not inc:
            break
    return


# Define 'a' < ... < 'z' < '0' < ... < '9'
def increase(a):
    if a == '9':
        return 'a', True
    if a == 'z':
        return '0', False
    return chr(ord(a) + 1), False


def max_str():
    r = ''
    for i in range(MAX_LENGTH):
        r += '9'
    return r


def min_str():
    r = ''
    for i in range(MAX_LENGTH):
        r += 'a'
    return r


def search_for_url(url_str, max_length):
    post_data = {'url': url_str}
    r = requests.post(POST_URL, data=post_data)
    logger.info('Get shortened: ' + r.text)
    l = len(r.text)
    if len(r.text) > max_length:
        return None
    return r.text


def is_a_page_exist(url):
    r = requests.get(url)
    logger.info('Get status code: ' + str(r.status_code))
    if r.status_code == 404:
        return False
    return True


def main_loop():
    logger.info('Loop start.')
    global global_str
    while True:
        change_global_str()
        logger.info('Start checking ' + global_str + '...')
        if not global_str:
            break
        t = search_for_url(POST_URL_PREFIX + global_str, MAX_URL_LENGTH)
        if t is not None and not is_a_page_exist(GET_URL_PREFIX + global_str):
            print(str, t)


logger = logging.getLogger('C0000_LOGGER')
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(funcName)s %(message)s',
                    datefmt='%H:%M:%S')
try:
    main_loop()
except KeyboardInterrupt:
    print('\nProgram finished.')
    print('Copyright (c) 2016 Hexapetalous. All rights reserved.')
