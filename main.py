from jdlogger import logger
import requests
import time
from PIL import Image
import matplotlib.pyplot as plt
import threading



class JDSecKill(object):

    def __init__(self):
        self.name = 'jdSecKill'
        self.isLogin = False
        self.qr_token = ''
        self.qr_cookie = ''

        self.session = requests.session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        self.session.cookies['cookie'] = ""

    def login(self):
        target_url = 'https://order.jd.com/center/list.action'

        resp = self.session.get(url=target_url, allow_redirects=False)

        if resp.status_code != requests.codes.OK:
            print(resp.status_code)
            self.login_by_scan_qrcode()
        else:
            self.isLogin = True
            logger.info('login successfully by cookies')

    def login_by_scan_qrcode(self):

        logger.info('start to get qrcode')

        qrcode_url = f"https://qr.m.jd.com/show?appid=133&size=147&t={round(time.time())}"
        qr_resp = self.session.get(qrcode_url)
        self.qr_cookie = qr_resp.cookies.get_dict()
        self.qr_token = self.qr_cookie['wlfstk_smdl']

        print(self.qr_token)
        print(self.qr_cookie)

        #check qrcode status
        threading.Thread(target=self.check_qrcode_status).start()

        #open qrcode
        with open('qrCode.jpg', 'wb')as f:
            f.write(qr_resp.content)
        img = Image.open('qrCode.jpg')
        plt.figure('qrcode')
        plt.imshow(img)
        plt.show()

    def check_qrcode_status(self):
        checkUrl = f'https://qr.m.jd.com/check?callback=jQuery4643268&appid=133&token={self.qr_token}&_={round(time.time() * 10000)}'

        while True:
            time.sleep(1)
            print(self.qr_token)


    def select_items(self):

        logger.info('select all items')

    def buy_items(self):
        logger.info('add items into cart')
        logger.info('select all itmes and ')
        logger.info('settlement')
        logger.info('submit order')


if __name__ == "__main__":
    jd = JDSecKill()
    jd.login()
    jd.select_items()
    jd.buy_items()
    time.sleep(100000)
