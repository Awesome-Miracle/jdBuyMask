import requests

if __name__ == "__main__":
    sess = requests.session()

    sess.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "TE": "Trailers"
    }

    resp = sess.get(url="https://www.jd.com/")

    cookies_dict = requests.utils.dict_from_cookiejar(sess.cookies)
    print(cookies_dict)
    print(resp.text)

    resp = sess.get(url="https://www.jd.com/")

    cookies_dict = requests.utils.dict_from_cookiejar(sess.cookies)
    print(cookies_dict)