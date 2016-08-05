# -*- coding: utf-8 -*-
"""
Application helpers
"""

import re
import sys
import urllib.request
from time import time


def gather_information(url):
    """Gather information about given url"""

    if not re.search(r'^https?://', url):
        url = 'http://' + url

    data = {'url' : url}

    request = urllib.request.Request(url, headers={'Accept-Encoding': 'gzip/deflate'})
    stream = urllib.request.urlopen(request)

    data['start_time'] = time()
    output = stream.read()
    info = stream.info()
    data['end_time'] = time()
    stream.close()

    data['loading_time'] = data['end_time'] - data['start_time']
    data['page_size'] = sys.getsizeof(output)

    return data
