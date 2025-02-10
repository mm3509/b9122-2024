import bs4


import exercise8_data


def get_product_title(url):
    """
    Get the product title from a URL on Amazon.

    # TODO: add doc-tests.
    """

    # TODO: change this to False if you have issues getting the HTML
    # from the web.
    get_html_web = True
    if get_html_web:
        html = exercise8_data.get_html(url)
    else:
        with open("exercise8.html") as f:
            html = f.read()

    # TODO: complete this function.
    return None
