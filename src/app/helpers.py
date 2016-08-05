# -*- coding: utf-8 -*-
"""
Application helpers
"""

import re
import sys
from phantomas import Phantomas


def gather_information(url):
    """Gather information about given url"""

    if not re.search(r'^https?://', url):
        url = 'http://' + url

    results = Phantomas(
        url=url,
        modules=['requestsStats']
    ).run()

    data = results.get_metrics()
    data['url'] = url

    return data
