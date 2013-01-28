repeat
======

Repeat command N times every S seconds.

Installation
------------
    $ pip install repeat

Usage
-----

    usage: repeat [-h] [-n N] [-s S] ...

    Repeat command N times every S seconds.

    positional arguments:
      cmd         Command to be repeated.

    optional arguments:
      -h, --help  show this help message and exit
      -n N        repeat N times. (default=10)
      -s S        repeat every S seconds. (default=1)

Example
-------
    
    # Display disk space every 2 seconds, but stops in 5 times.
    $ repeat -n 5 -s 2 df -h
    
Author
------
- Park, Hyunwoo \<ez.amiryo at gmail.com\>
- Eunchong Yu \<kroisse at gmail.com\>

Disclaimer
----------
Distributed under MIT license.
And use at your own risk. This was not tested carefully.
