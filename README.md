## Page loading time

This is an exemple of a web application that take a list of urls and rank them by loading time and page size.

### Usage

Set the file `urls.json` to set the list of urls to load.

Then just start the server:
```bash
python server.py
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

### Unit testing

You can use the unittest python module in command line to test the application:
```bash
python -m unittest tests/*.py
```

To unit test when using a docker image, you can use the exec command or specify a shell when running the container
```bash
docker exec -ti some_container_name python -m unittest tests/*.py
```
