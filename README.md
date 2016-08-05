## Page loading time

This is an exemple of a web application that take a list of urls and rank them by loading time and page size.

This version uses [phantomas](https://github.com/macbre/phantomas). Make sure you have it installed and in your path or use the Docker image decribed below.

### Usage

Set the file `urls.json` to set the list of urls to load.

Then just start the server:
```bash
python server.py
```

### Unit testing

You can use the unittest python module in command line to test the application:
```bash
python -m unittest tests/*.py
```

### Docker image

Build:
```bash
docker build -t corentingi/page-loading-time .
```

Run with debug:
```bash
docker run --rm -ti -p 8080:8080 -e APP_DEBUG=True corentingi/page-loading-time
```
