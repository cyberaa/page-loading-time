from bottle import route, get, post, run, request, template
import json
import os
from selenium import webdriver

@get('/')
def index():
    return 'Hi!'

@get('/selenium')
def index():
    browser = webdriver.Chrome()
    browser.get('http://seleniumhq.org/')

    return browser.title

@get('/time')
def time():
    if not 'u' in request.query:
        return 'No url given'

    # return json.dumps(browser.title, indent=2, separators=(',', ': '))
    return request.query['u']

if __name__ == '__main__':
    run(host='0.0.0.0', port=80)
