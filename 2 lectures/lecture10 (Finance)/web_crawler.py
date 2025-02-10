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


def clean_and_join_url(url, href):
    """
    >>> clean_and_join_url("http://example.com", "/new_page#someId")
    'http://example.com/new_page'
    >>> clean_and_join_url("http://example.com", "/new_page?someParam=value")
    'http://example.com/new_page'
    """


    for marker in ["#", "?"]:
        trim_index = href.find(marker)
        if -1 != trim_index:
            href = href[:trim_index]
   

    return urllib.parse.urljoin(url, href)


def should_visit_url(url, seed_url):

    if not url.startswith(seed_url):
        return False

    if url.endswith(".pdf"):
        return False

    return True


def get_links(url):

    html = get_webpage(url)
    if not html:
        return []

    soup = bs4.BeautifulSoup(html, "html.parser")

    all_urls = []
    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        new_url = clean_and_join_url(url, href)
        all_urls.append(new_url)

    return all_urls


def crawl(seed_url):

    queue = [seed_url]
    visited = []

    while len(queue) > 0:

        if MAX_URLS < len(visited):
            print("  Reached maximum of %d URLs visited, exiting" % MAX_URLS)
            return

        # Note: here is a good for .pop() instead o .remove()!
        url = queue.pop()

        if url in visited:
            #print("  Skipping visited link: " + url)
            continue

        if not should_visit_url(url, seed_url):
            #print("  Skipping link outside of policies: " + url)
            continue

        print("Visited: %d, to visit: %d, visiting: %s" %
              (len(visited), len(queue), url))

        new_links = get_links(url)
        visited.append(url)

        # Add only unique links to the list to visit. I don't use
        # set() so we visit the links in the order they were
        # discovered.
        for link in new_links:
            if link not in queue:
                queue.append(link)


def main():
    args = sys.argv
    if 2 != len(args):
        print("Usage: python3 web_crawler.py <URL>")
        return

    seed_url = sys.argv[1]
    return crawl(seed_url)


if '__main__' == __name__:
    doctests = doctest.testmod(optionflags=doctest.ELLIPSIS)
    assert 0 == doctests.failed, 'Some doc-tests failed, exiting...'
    main()
