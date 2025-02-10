# Don't submit this file.

import os


import requests


SAMPLE_URLS = [
    "https://www.amazon.com/Practical-Guide-Quantitative-Finance-Interviews/dp/1438236662",  # noqa: E501
    "https://www.amazon.com/Mostly-Harmless-Econometrics-Empiricists-Companion/dp/0691120358",  # noqa: E501
    "https://www.amazon.com/Tale-Two-Cities-Charles-Dickens/dp/145153194X"
]


def dump(html, filename="exercise8.html"):
    fp = os.path.join(filename)

    with open(fp, "w+") as f:
        f.write(html)

    print("Saved HTML to this file for you to debug: " + fp)

    return fp


def get_cached_html(url):
    if url not in SAMPLE_URLS:
        return None

    fn = "exercise8_%d.html" % SAMPLE_URLS.index(url)
    fp = os.path.join(os.path.dirname(__file__), fn)
    if not os.path.exists(fp):
        return None

    with open(fp) as f:
        return f.read()


def get_html(url):

    cached = get_cached_html(url)
    if cached:
        return cached

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",  # noqa: E501
        "X-Requested-With": "XMLHttpRequest"
    }
    response = requests.get(url, headers=headers)

    return response.text


# Students: ignore the rest of this file: it's for Autograder.
if "__main__" == __name__:
    for i, url in enumerate(SAMPLE_URLS):
        html = get_html(url)
        dump(html, filename="exercise8_%d.html" % i)
