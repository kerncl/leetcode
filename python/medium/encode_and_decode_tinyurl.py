"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
"""
import sys
import logging
import random


class Codec:

    def __init__(self):
        self.cache = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = longUrl + str(random.randint(0,100))
        if shortUrl in self.cache:
            return shortUrl
        self.cache[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.cache.get(shortUrl, 'Invalid Url')

    def __str__(self):
        return ','.join(self.cache.values())


if __name__ == '__main__':
    log = logging.getLogger()
    log.setLevel(logging.INFO)

    format = '%(asctime)s [%(levelname)s]: %(message)s'
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(logging.Formatter(format))
    stream.setLevel(logging.INFO)
    log.addHandler(stream)

    url = "https://leetcode.com/problems/design-tinyurl"
    urldecode = Codec()
    shortURL = urldecode.encode(url)
    assert shortURL == urldecode.decode(shortURL), log.error(f'Invalid link')

    while log.handlers:
        handler = log.handlers[0]
        handler.close()
        log.removeHandler(handler)