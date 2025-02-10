import requests

def get_html(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",  # noqa: E501
        "X-Requested-With": "XMLHttpRequest"
    }
    response = requests.get(url, headers=headers)

    with open("output.html", "w+") as f:
        f.write(response.text)
