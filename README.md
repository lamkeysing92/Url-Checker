Just uploading a newer version of the older fork that doesn't work in Python3.
I changed the code to be a lil bit more performing than the older version.

This program makes use of the wonderful requests and docopt libraries.
Install dependencies with either

    pip install -r requirements.txt

or

    pip install requests
    pip install docopt

How to use:

    Usage:
    main.py <file> <url> [-a]
    main.py <file> <url>

    This program brute forces a url pattern, with words from a provided
    file, to detect anything that does not throw a 404 error. Useful for
    finding hidden directories and files. A good number of wordlists have
    been included in this distribution for your convenience.

    Examples:
        main.py wordlist.txt http://www.example.com/\{\}/
        main.py wordlist.txt http://www.example.com/\{\}.php --async
        main.py wordlist.txt http://www.example.com/file.php?argument=\{\}

    Options:
        -h, --help      Display this message
        -v, --version   Display the version of this program
        file            File to read wordlist/url patterns from [required]
        url             Url to run against [required]
        -a, --async     Send requests asynchronously (faster but straining on server)
