from selenium import webdriver
import time
import json


if __name__ == "__main__":

    driver = webdriver.Chrome()

    driver.get("https://passport.jd.com/new/login.aspx")

    current_cookie_str =""

    while True:

        cookies = driver.get_cookies()
        c = [item["name"] + "=" + item["value"] for item in cookies]
        cookie_str = '; '.join(item for item in c)

        if current_cookie_str != cookie_str:
            current_cookie_str = cookie_str
            print(current_cookie_str)

        time.sleep(5)

