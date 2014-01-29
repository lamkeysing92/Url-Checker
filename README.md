wfuzz was throwing errors for me, so I thought I'd do what any sane programmer would do, make my own version from scratch!

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
