import bs4


import exercise8_data


def get_product_title(url):
    """
    >>> get_product_title("https://www.amazon.com/Practical-Guide-Quantitative-Finance-Interviews/dp/1438236662")
    'A Practical Guide To Quantitative Finance Interviews'
    >>> get_product_title(123)
    Traceback (most recent call last):
    ...
    ValueError: argument must be a string
    >>> get_product_title('https://www.google.com')
    Traceback (most recent call last):
    ...
    ValueError: argument must be an Amazon link
    """
    
    if not isinstance(url, str):
        raise ValueError("argument must be a string")

    if not url.startswith("https://www.amazon.com/"):
        raise ValueError("argument must be an Amazon link")

    html = exercise8_data.get_html(url)

    soup = bs4.BeautifulSoup(html, "html.parser")

    titles = soup.select("span#productTitle")
    if 1 != len(titles):
        print("No unique div tag for %s! Found %d" % (url, len(titles)))
        print(html)
        assert False

    return titles[0].get_text().strip()

