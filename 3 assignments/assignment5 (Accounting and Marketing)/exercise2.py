import doctest
import sys
import time
import urllib.request


import bs4  # If needed, install with: `pip install bs4`


USER_AGENT_KEY = "User-Agent"
USER_AGENT_VALUE = ("Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0)"
                    " Gecko/20100101 Firefox/10.0")

MAX_URLS = 500
SEED_URL = "https://www.apple.com/newsroom"


def is_url_valid(url):
    """
    >>> is_url_valid("https://www.apple.com")
    True
    >>> is_url_valid(123)
    False
    >>> is_url_valid("javascript:void(0)")
    False
    >>> is_url_valid("mailto:email@email.com")
    False
    >>> is_url_valid("tel:+12345678900")
    False
    """

    # TODO: complete this function to pass the tests. You should then
    # find one place in the file where to call this function.

    return


def get_webpage(url):
    req = urllib.request.Request(url)
    req.add_header(USER_AGENT_KEY, USER_AGENT_VALUE)

    try:
        html = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError:
        print("  Skipping URL that throws an error: " + url)
        return

    return html


def clean_url(url):
    """
    >>> clean_url("http://example.com/new_page#someId")
    'http://example.com/new_page'
    >>> clean_url("http://example.com/new_page?someParam=someValue")
    'http://example.com/new_page'
    >>> clean_url("https://www.apple.com/newsroom/")
    'https://www.apple.com/newsroom'
    """

    for marker in ["#", "?"]:
        trim_index = url.find(marker)
        if -1 != trim_index:
            url = url[:trim_index]

    return url


def join_url(url, href):
    """
    >>> join_url("http://example.com", "/root_relative_link")
    'http://example.com/root_relative_link'
    >>> join_url("http://example.com/docs/", "relative_link")
    'http://example.com/docs/relative_link'
    >>> join_url("http://example.com", "https://absolute-link.com")
    'https://absolute-link.com'
    """

    return urllib.parse.urljoin(url, href)


def should_visit_url(url, seed_url):
    """
    >>> should_visit_url("https://www.google.com", "https://www.apple.com")
    False
    >>> should_visit_url("javascript(void:0)", "https://www.apple.com")
    False
    >>> should_visit_url("https://www.apple.com/statement.pdf", "https://www.apple.com")  # noqa: E501
    False
    >>> should_visit_url("https://www.apple.com/statement.zip", "https://www.apple.com")  # noqa: E501
    False
    >>> should_visit_url("https://www.apple.com/statement.mp4", "https://www.apple.com")  # noqa: E501
    False
    >>> should_visit_url("https://www.apple.com/newsroom", "https://www.apple.com")
    True
    """

    if seed_url not in url:
        return False

    # TODO: modify this to skip the following filetypes: .zip, .mp4, .pdf

    return True


def url_to_soup(url):
    html = get_webpage(url)
    if html is None:
        return

    return bs4.BeautifulSoup(html, "html.parser")


def get_links(url):

    soup = url_to_soup(url)
    if not soup:
        return []

    all_urls = []
    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        new_url = clean_url(join_url(url, href))
        all_urls.append(new_url)

    return all_urls


def is_press_release(url):
    """
    >>> is_press_release("https://www.apple.com/newsroom/2024/10/apple-reports-fourth-quarter-results/")  # noqa: E501
    True
    >>> is_press_release("https://www.apple.com/newsroom/2024/11/apple-debuts-the-weeknds-immersive-music-experience-for-apple-vision-pro/")  # noqa: E501
    False
    >>> is_press_release("https://www.apple.com/newsroom/2024/10/new-macbook-pro-features-m4-family-of-chips-and-apple-intelligence/")  # noqa: E501
    True
    """

    soup = url_to_soup(url)  # noqa: F841

    # TODO: complete this function.

    return False


def crawl(seed_url, sleep_delay=0):

    # TODO: collect the URLs that are press releases.

    queue = [seed_url]
    visited = set()

    while len(queue) > 0:

        if MAX_URLS < len(visited):
            print("  Reached maximum of %d URLs visited, exiting" % MAX_URLS)
            break

        # Note: here is a good for .pop() instead of .remove()!  This
        # pops the last item in the queue, which is more efficient. So
        # this is a Last-In-First-Out queue (LIFO), also called
        # "depth-first-search".
        url = queue.pop()

        if url in visited:
            print("  Skipping visited link: " + url)
            continue

        if not should_visit_url(url, seed_url):
            print("  Skipping link outside of policies: " + url)
            continue

        print("Visited: %d, to visit: %d, visiting: %s" %
              (len(visited), len(queue), url))

        # Students: we pause the code here to slow down the requests,
        # otherwise Autograder may make too many requests to the Apple
        # website and it may become blacklisted. Do not delete this
        # line.  The default value of 0 ensures your code runs fast on
        # your machine, and can run more slowly when Autograder calls
        # it.
        time.sleep(sleep_delay)

        new_links = get_links(url)

        # Students: these lines are slightly different from lecture
        # because we use built-in sets instead of lists.
        visited.add(url)
        unvisited_links = set(new_links) - set(queue) - visited
        queue.extend(list(unvisited_links))

    return


def main():
    press_releases = crawl(SEED_URL)
    print(press_releases)


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
    main()
