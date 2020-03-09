from selenium import webdriver
import time
import json
import requests


if __name__ == "__main__":

    driver = webdriver.Chrome()

    driver.get("https://passport.jd.com/new/login.aspx")

    cookie_str =""

    while True:

        try:
            a = driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div/div[1]/div[2]/p[1]")

            if a.text[0:3] == "Hi，":
                cookies = driver.get_cookies()
                c = [item["name"] + "=" + item["value"] for item in cookies]
                cookie_str = '; '.join(item for item in c)
                break

        except Exception:
            print('Not login')

        time.sleep(3)

    print(cookie_str)

    sess = requests.session()

    sess.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Cookie": cookie_str,
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "TE": "Trailers"
    }

    resp = sess.get(url="https://order.jd.com/center/list.action")

    print(requests.utils.get_encodings_from_content(resp.text))
    print(resp.apparent_encoding)
    #
    print(resp.text)



