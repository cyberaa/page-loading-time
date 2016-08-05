## Page loading time

This is an exemple of a web application that take a list of urls and rank them by loading time and page size.

This branch uses the [phantomas](https://github.com/macbre/phantomas) tool base on phantomjs.
Make sure you have it installed and in your path or use the Docker image decribed below.

### Usage

Set the file `urls.json` with the list of urls to load. (The `urls-example.json` file is here to help)

Then just start the server:
```bash
python server.py
```

The following environement variable are available:
- APP_HOST (default=localhost)
- APP_PORT (default=8080)
- APP_DEBUG (defaul=False)

### Docker image

Build:
```bash
docker build -t corentingi/page-loading-time:phantomas .
```

Run with debug:
```bash
docker run --rm -ti -p 8080:8080 -e APP_DEBUG=True corentingi/page-loading-time:phantomas
```

### Unit testing

You can use the unittest python module in command line to test the application:
```bash
python -m unittest tests/*.py
```

To unit test when using a docker image, you can use the exec command or specify a shell when running the container
```bash
docker exec -ti some_container_name python -m unittest tests/*.py
```
