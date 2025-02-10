import doctest
import sys
import urllib.request


import bs4  # pip install bs4


USER_AGENT_KEY = "User-Agent"
USER_AGENT_VALUE = ("Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0)"
                    " Gecko/20100101 Firefox/10.0")

MAX_URLS = 200


def get_webpage(url):
    req = urllib.request.Request(url)
    req.add_header(USER_AGENT_KEY, USER_AGENT_VALUE)

    try:
        html = urllib.request.urlopen(req).read()
    except urllib.error.HTTPError:
        print("  Skipping URL that gives an error: " + url)
        return

    return html


def clean_url(url):
    """
    >>> clean_url("http://example.com/new_page#someId")
    'http://example.com/new_page'
    >>> clean_url("http://example.com/new_page?someGetParameter=someValue")
    'http://example.com/new_page'
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
    
    if not url.startswith(seed_url):
        return False

    if url.endswith(".pdf"):
        return False

    return True


def get_links(url):

    html = get_webpage(url)
    if html is None:
        return []

    soup = bs4.BeautifulSoup(html, "html.parser")

    all_urls = []
    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        new_url = clean_url(join_url(url, href))
        all_urls.append(new_url)

    return all_urls


def crawl(seed_url):

    queue = [seed_url]
    visited = set()

    while len(queue) > 0:

        if MAX_URLS < len(visited):
            print("  Reached maximum of %d URLs visited, exiting" % MAX_URLS)
            return

        # Note: here is a good for .pop() instead of .remove()!
        url = queue.pop()

        if not should_visit_url(url, seed_url):
            print("  Skipping link outside of policies: " + url)
            continue

        print("Queue length: %d, treated: %d visiting: %s" %
              (len(queue), len(treated), url))

        new_links = get_links(url)
        visited.add(url)

        # Students: use built-in sets, which guarantee uniqueness.
        unvisited_links = set(new_links) - set(queue) - visited
        queue.extend(list(unvisited_links))


def main():

    # Default value, in case you run inside PyCharm.
    seed_url = "https://openclimatecurriculum.org"
    args = sys.argv
    # if 1 < len(args):
    #     seed_url = args[1]
    
    return crawl(seed_url)


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'

main()
