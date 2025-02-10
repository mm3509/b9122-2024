import bs4
import os
import requests
import subprocess

# TODO: change these values to suit your case.
URL = "https://www.ebay.com/itm/156425666332"
MAX_PRICE = 20
PRICE_START = "US $"
DEBUG = False


def dump(html):
    fp = os.path.join(os.path.expanduser("~"),
                      "Downloads",
                      "scraper_debug.html"
                      )
    with open(fp, "w+") as f:
        f.write(html)

    print("Saved HTML to file for you to debug: " + fp)

    return fp


def get_html(url=URL, no_user_agent=True):

    print("Getting the HTML from the web...")

    if no_user_agent:
        response = requests.get(url)
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        response = requests.get(url, headers=headers)
        
    return response.text


def get_price(url=URL):

    html = get_html(url)

    soup = bs4.BeautifulSoup(html, "html.parser")

    content_tags = soup.select("div#mainContent")

    assert len(content_tags) == 1, "Code more"

    content = content_tags[0]

    price_tags = content.select("div.x-price-primary")

    assert len(price_tags) == 1, "Code more: price tags = " + str(len(price_tags))

    price_text = price_tags[0].get_text()

    price_float = float(price_text.replace(PRICE_START, ""))
    
    return price_float
    

if "__main__" == __name__:
    try:
        price = get_price(URL)
    except IndexError:
        print("Got an error!! Please debug.")
        html = get_html(URL)
        dump(html)
    else:
        if price < MAX_PRICE:
            subprocess.check_output("open " + URL, shell=True)

# Include this into crontab to run every day at 2.30pm with:
# cat <(crontab -l) <(echo "0 12 * * * python $HOME/b9122/lecture5/scraper.py") | crontab -
