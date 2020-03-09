import requests
import time
from PIL import Image
import matplotlib.pyplot as plt

proxies = {"http":"http://127.0.0.1:8888","https":"http://127.0.0.1:8888"}
cert_file = "./fiddler.crt"


if __name__ == "__main__":

    sess = requests.session()

    sess.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "TE": "Trailers"
    }

    # # url = "https://order.jd.com/center/list.action"
    # url = "https://passport.jd.com/new/login.aspx"
    # # resp = sess.get(url=url, proxies=proxies, verify=cert_file, allow_redirects=False)
    # resp = sess.get(url=url, proxies=proxies, verify=cert_file)
    # # resp = sess.get(url=url, allow_redirects=False)
    # # resp = sess.get(url=url)
    # print(resp.status_code)
    # print(resp.text)


    url = f"https://qr.m.jd.com/show?appid=133&size=147&t={round(time.time())}"
    # resp = requests.get(url, proxies=proxies, verify=cert_file)
    # resp = sess.get(url, proxies=proxies, verify=cert_file)
    resp = sess.get(url)
    # resp = requests.get(url)
    print(resp.status_code)
    # open qrcode
    with open('qrCode.jpg', 'wb')as f:
        f.write(resp.content)

    img = Image.open('qrCode.jpg')
    plt.figure('qrcode')
    plt.imshow(img)
    plt.show()

    #sleep 20s
    time.sleep(20)


