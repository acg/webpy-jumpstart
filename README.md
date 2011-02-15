# Jump start web.py + lighttpd + FastCGI #

This is a simple [web.py](http://webpy.org/) app that should get you up and running with the [lighttpd](http://www.lighttpd.net/) web server and FastCGI.

## Requirements ##

* web.py
* lighttpd
* daemontools (optional)

## Running it ##

If you have daemontools:

    svscan svc

Otherwise

    cd svc/lighttpd
    ./run

Now go to [http://127.0.0.1:8084](http://127.0.0.1:8084).

You should see something like this:

    Request number 1 for path / query  for pid 123456

If you refresh again:

    Request number 2 for path / query  for pid 123456

As you can see, there's a stateful counter that persists across requests.

There are actually 2 FastCGI server processes running, but the first one is so fast in this minimal example you're not likely to get directed to the second. Put a `time.sleep(0.5)` in the `GET` method to see the second process get involved.

