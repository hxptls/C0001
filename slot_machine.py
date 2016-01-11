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
import requests.exceptions
import logging
import time


class SlotMachine(object):
    logger = None
    # This program will try to access the url from '!!!' (33 in ASCII) to '~~~'
    # (126 in ASCII), the length of string depends on the constant below. Many
    # of these url are illegal, but I don't care.
    MAX_LENGTH = 3
    current_string = ""

    def logger_init(self, level):
        logger = logging.getLogger('Logger')
        log_format = logging.Formatter(
            '%(asctime)s [%(levelname)s]%(funcName)s %(message)s',
            '%Y-%m-%d %H:%M:%S')
        file_handle = logging.StreamHandler()
        file_handle.setFormatter(log_format)
        logger.addHandler(file_handle)
        logger.setLevel(level)  # Why I can't set level from handler! *_*
        self.logger = logger
        self.logger.debug('Logger is inited.')
        return

    def string_init(self):
        self.current_string = '!'
        for i in range(1, self.MAX_LENGTH):
            self.current_string += ' '
        return

    IGNORED_CHARACTERS = '\"%\'()./:;I[\\]^`|{}'

    def increase_string(self):
        flag = 1
        for i in range(self.MAX_LENGTH):
            t = ord(self.current_string[i]) + 1
            while chr(t) in self.IGNORED_CHARACTERS:
                t += 1
            t = chr(t)
            if t <= '~':
                flag = 0
            else:
                t = '!'
            self.current_string = \
                self.current_string[:i] + t + self.current_string[i + 1:]
            if not flag:
                break
        if flag:
            return False  # No more string.
        return True

    def check_url(self, url):
        try:
            r = requests.get(url, timeout=10)
        except requests.exceptions.RequestException:
            self.logger.error('Failed when checking: %s' % url)
            time.sleep(5)  # Maybe help.
            return None
        if r.status_code == 404 and r.url != url:
            return r.url
        if r.url == url:
            self.logger.debug('Can not resolve url: %s' % r.url)
        return None

    URL_PREFIX = 'http://git.io/'

    def make_url(self, string):
        stri = ""
        for i in range(self.MAX_LENGTH):
            if string[i] == ' ':
                break
            else:
                stri = stri[:i] + string[i] + stri[i + 1:]
        return self.URL_PREFIX + stri

    def __init__(self):
        super(SlotMachine, self).__init__()
        self.logger_init(logging.INFO)
        self.string_init()
        return

    def main_loop(self):
        while True:
            url = self.make_url(self.current_string)
            self.logger.debug('Checking %s ...' % url)
            u = self.check_url(url)
            if u is not None:
                print(url, '->', u)
            if not self.increase_string():
                break
            time.sleep(0.2)


if __name__ == '__main__':
    s = SlotMachine()
    try:
        s.main_loop()
    except KeyboardInterrupt:
        print('\nCopyright (c) 2016 Hexapetalous. All rights reserved.')
