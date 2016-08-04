whoami
======

Basic python container that runs a http server that prints the container id (the
host name). Inspired by jwilder/whoami. This container is based on python:alpine
and as such is smaller.

    $ docker run -d -p 8000:8000 -t thrawny/whoami --name whoami

    $ curl dockerip:8000
    c44b4d869a84
