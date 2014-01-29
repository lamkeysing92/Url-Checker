""" Usage:
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

"""

import requests
from docopt import docopt
import time
import grequests


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def main(file, url, async):
    f = open(file, 'r')
    num_lines = file_len(file)
    start_time = time.time()

    print "Checking {} different urls, this may take a while.\n".format(num_lines)

    urls = []
    for line in f:
        line = line.rstrip('\n')
        formated_url = url.format(line)
        urls.append(formated_url)
    if async:
        rs = (grequests.get(u) for u in urls)
        responses = grequests.map(rs)
        for response in responses:
            if response.status_code != 404:
                print response.url
                print response.status_code
                print
    else:
        for url in urls:
            r = requests.get(formated_url, verify=False)
            if r.status_code != 404:
                print r.url
                print r.status_code
                print

    print "Checked {} different urls in {} seconds\n".format(num_lines, time.time() - start_time)


if __name__ == '__main__':
    arguments = docopt(__doc__, version="0.2")
    main(arguments['<file>'], arguments['<url>'], arguments['--async'])

